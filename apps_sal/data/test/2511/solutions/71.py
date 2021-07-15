mod = 10 ** 9 + 7

n, k = map(int, input().split())
edge = [[] for _ in range(n)]
parent = [0] * n
permutation_k2 = [1] * n
for i in range(n-1):
  a, b = map(int, input().split())
  edge[a-1].append(b-1)
  edge[b-1].append(a-1)
  permutation_k2[i+1] = permutation_k2[i] * (k - 2 - i) % mod
count = k * (k - 1) * permutation_k2[len(edge[0]) - 1] % mod
queue = edge[0]
while queue:
  vertex = queue.pop()
  count = count * permutation_k2[len(edge[vertex]) - 1] % mod
  p = parent[vertex]
  for v in edge[vertex]:
    if v == p:
      continue
    queue.append(v)
    parent[v] = vertex
if n == 1:
  print(k)
else:
  print(count)
