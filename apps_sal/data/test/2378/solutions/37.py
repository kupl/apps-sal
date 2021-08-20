import sys
readline = sys.stdin.readline
N = int(readline())
graph = [[] for _ in range(N + 1)]
for i in range(N - 1):
    (a, b) = map(int, readline().split())
    graph[a].append(b)
    graph[b].append(a)
parent = [0] * (N + 1)
order = []
stack = [1]
while stack:
    x = stack.pop()
    order.append(x)
    for y in graph[x]:
        if y == parent[x]:
            continue
        parent[y] = x
        stack.append(y)
MOD = 10 ** 9 + 7
half = pow(2, MOD - 2, MOD)
power_inv = [1] * (N + 1)
size = [1] * (N + 1)
for (i, v) in enumerate(order[::-1], 1):
    p = parent[v]
    x = size[v]
    size[p] += x
    power_inv[i] = power_inv[i - 1] * half % MOD
ans = sum(((1 - power_inv[i] - power_inv[N - i] + power_inv[N]) % MOD for i in size[2:]))
ans += 1 - power_inv[N] - N * power_inv[1]
ans %= MOD
print(ans)
