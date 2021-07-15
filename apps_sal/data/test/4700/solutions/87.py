N, M = map(int, input().split())
H = [0] + list(map(int, input().split()))

g = [[] for _ in range(N+1)]
for i in range(M):
  a, b = map(int, input().split())
  g[a].append(b)
  g[b].append(a)

ans = 0
for j in range(1, N+1):
  for k in g[j]:
    if H[j] <= H[k]:
      break
  else:
    ans += 1
print(ans)
