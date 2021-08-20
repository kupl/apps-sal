from collections import deque
N = int(input())
ab = [list(map(int, input().split())) for _ in range(N - 1)]
mod = 10 ** 9 + 7
fact = [1] * (N + 1)
fact_inv = [1] * (N + 1)
for i in range(1, N + 1):
    fact[i] = fact[i - 1] * i % mod
fact_inv[-1] = pow(fact[-1], mod - 2, mod)
for i in range(N, 0, -1):
    fact_inv[i - 1] = fact_inv[i] * i % mod
g = [deque([]) for _ in range(N + 1)]
for (a, b) in ab:
    g[a].append(b)
    g[b].append(a)
parents = [0] * (N + 1)
q = deque([])
s = deque([1])
while s:
    x = s.pop()
    q.append(x)
    for y in g[x]:
        if y == parents[x]:
            continue
        else:
            parents[y] = x
            s.append(y)
q = list(q)
size_forward = [0] * (N + 1)
dp_forward = [1] * (N + 1)
for i in q[::-1]:
    p = parents[i]
    s = size_forward[i] + 1
    size_forward[p] += s
    dp_forward[i] *= fact[size_forward[i]]
    dp_forward[p] *= dp_forward[i] * fact_inv[s]
    dp_forward[p] %= mod
size_back = [N - 1 - i for i in size_forward]
dp_back = [1] * (N + 1)
for i in q[1:]:
    p = parents[i]
    x = dp_back[p]
    x *= fact_inv[size_back[p]]
    x *= dp_forward[p]
    x *= fact_inv[size_forward[p]]
    x *= fact[size_forward[i] + 1]
    x *= pow(dp_forward[i], mod - 2, mod)
    x *= fact[size_back[i] - 1]
    dp_back[i] = x % mod
for (a, b, c, d) in zip(size_forward[1:], dp_forward[1:], size_back[1:], dp_back[1:]):
    ans = b * d * fact[a + c] * fact_inv[a] * fact_inv[c]
    ans %= mod
    print(ans)
