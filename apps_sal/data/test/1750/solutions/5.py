from collections import deque

n = int(input())

ans = [0]*n

g = [[]for _ in range(n)]

for _ in range(n - 1):
  u, v = list(map(int, input().split()))
  u -= 1
  v -= 1
  g[u].append(v)
  g[v].append(u)

col = 1
q = deque()
vis = [False]*n

q.append((0, 0))
vis[0] = True
ans[0] = 1
p_top = 0

while q:
  top, p_top = q.popleft()
  col = 1
  for viz in g[top]:
    if not vis[viz]:
      vis[viz] = True
      q.append((viz, top))
      while ans[top] == col or ans[p_top] == col:
        col += 1
      ans[viz] = col
      col += 1

print(max(ans))
print(" ".join(map(str, ans)))

