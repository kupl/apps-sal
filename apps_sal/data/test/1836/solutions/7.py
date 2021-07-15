def read(): return list(map(int, input().split()))
n, m = read()
lst = [[] for _ in range(n + 1)]
for _ in range(m):
  u, v = read()
  lst[u].append(v)
  lst[v].append(u)
d = [1] * (n + 1)
ans = 0
for v in range(1, n + 1):
  ans = max(ans, d[v] * len(lst[v]))
  for u in lst[v]:
    if u > v:
      d[u] = max(d[u], d[v] + 1)
print(ans)
