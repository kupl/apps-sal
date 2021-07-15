n,m = map(int,input().split())
h = list(map(int,input().split()))

g = [[] for _ in range(n)]
for _ in range(m):
  a,b = map(int,input().split())
  g[a-1].append(b-1)
  g[b-1].append(a-1)

cnt = n
for i in range(n):
  for j in g[i]:
    if h[i] <= h[j]:
      cnt -= 1
      break
print(cnt)
