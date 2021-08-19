n = int(input())
ab = [list(map(int, input().split())) for _ in range(n - 1)]
mod = 10 ** 9 + 7
MAX = n
fact = [1] * (MAX + 1)
for i in range(1, MAX + 1):
    fact[i] = fact[i - 1] * i % mod
inv = [1] * (MAX + 1)
for i in range(2, MAX + 1):
    inv[i] = inv[mod % i] * (mod - mod // i) % mod
fact_inv = [1] * (MAX + 1)
for i in range(1, MAX + 1):
    fact_inv[i] = fact_inv[i - 1] * inv[i] % mod
adj = [[] for _ in range(n + 1)]
for (a, b) in ab:
    adj[a].append(b)
    adj[b].append(a)
root = 1
stack = [root]
par = [0] * (n + 1)
order = []
while stack:
    u = stack.pop()
    order.append(u)
    for v in adj[u]:
        if v == par[u]:
            continue
        par[v] = u
        stack.append(v)
size_d = [0] * (n + 1)
dp_d = [1] * (n + 1)
for v in order[::-1]:
    dp_d[v] *= fact[size_d[v]]
    dp_d[v] %= mod
    s = size_d[v] + 1
    p = par[v]
    size_d[p] += s
    dp_d[p] *= fact_inv[s] * dp_d[v]
    dp_d[p] %= mod
size_u = [n - 2 - e for e in size_d]
dp_u = [1] * (n + 1)
for v in order[1:]:
    p = par[v]
    x = dp_d[p]
    x *= fact_inv[size_d[p]]
    x *= fact[size_d[v] + 1]
    x *= pow(dp_d[v], mod - 2, mod)
    x *= fact[size_u[v]]
    x *= fact_inv[size_u[p] + 1]
    x *= dp_u[p]
    dp_u[v] = x % mod
for (eu, su, ed, sd) in zip(dp_u[1:], size_u[1:], dp_d[1:], size_d[1:]):
    su += 1
    ans = eu * ed * fact[su + sd] * fact_inv[su] * fact_inv[sd] % mod
    print(ans)
