MOD = 10 ** 9 + 7

n = int(input())
edge = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)

fact = [1] * n
inverse = [1] * n
inv_fact = [1] * n
for i in range(2, n):
    fact[i] = fact[i - 1] * i % MOD
    inverse[i] = -inverse[MOD % i] * (MOD // i) % MOD
    inv_fact[i] = inv_fact[i - 1] * inverse[i] % MOD

stack = [0]
parent = [0] * n
route = []
while stack:
    vertex = stack.pop()
    route.append(vertex)
    for child in edge[vertex]:
        if parent[vertex] != child:
            parent[child] = vertex
            stack.append(child)

dp = [1] * n
size = [1] * n
for vertex in route[:0:-1]:
    pa = parent[vertex]
    sz = size[vertex]
    dp[vertex] = dp[vertex] * fact[sz - 1] % MOD
    dp[pa] = dp[pa] * dp[vertex] * inv_fact[sz] % MOD
    size[pa] += sz
dp[0] = dp[0] * fact[n - 1] % MOD

for vertex in route[1:]:
    pa = parent[vertex]
    sz = size[vertex]
    inv_dp = pow(dp[vertex], MOD - 2, MOD)
    dp[vertex] = dp[vertex] * dp[pa] * inv_dp * sz * inverse[n - sz] % MOD

for value in dp:
    print(value)
