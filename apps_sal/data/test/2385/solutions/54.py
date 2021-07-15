MOD = 10 ** 9 + 7
MAX_N = 2 * 10 ** 5

fact = [1] * MAX_N
inverse = [1] * MAX_N
inv_fact = [1] * MAX_N
for i in range(2, MAX_N):
  fact[i] = fact[i-1] * i % MOD
  inverse[i] = -inverse[MOD % i] * (MOD // i) % MOD
  inv_fact[i] = inv_fact[i-1] * inverse[i] % MOD

n = int(input())
edge = [[] for _ in range(n)]
for _ in range(n-1):
  a, b = map(int, input().split())
  edge[a-1].append(b-1)
  edge[b-1].append(a-1)

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
  dp[vertex] = dp[vertex] * fact[sz-1] % MOD
  dp[pa] = dp[pa] * dp[vertex] * inv_fact[sz] % MOD
  size[pa] += sz
dp[0] = dp[0] * fact[n-1] % MOD

for vertex in route[1:]:
  pa = parent[vertex]
  sz = size[vertex]
  tmp = dp[pa] * pow(dp[vertex], MOD - 2, MOD) * sz * inverse[n-sz] % MOD
  dp[vertex] = dp[vertex] * tmp % MOD

for value in dp:
  print(value)
