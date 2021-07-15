N, *L = map(int, open(0).read().split())
cost = []
for i,m in enumerate(zip(*[iter(L)]*N)):
  cost.append(list(m))
  cost[i][i] = 10**10
ans = 0
for i in range(N):
  for j in range(i):
    m = min(a+b for a, b in zip(cost[i],cost[j]))
    if m<cost[i][j]:
      print(-1)
      return
    if m>cost[i][j]:
      ans += cost[i][j]
print(ans)
