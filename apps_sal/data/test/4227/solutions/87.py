def dfs(v, used):
  if not False in used: return 1
  ans = 0
  for i in range(n):
    if not matrix[v][i]: continue
    if used[i]: continue
    used[i] = True
    ans += dfs(i, used)
    used[i] = False
  return ans

n, m = map(int, input().split())
matrix = [[0]*n for _ in range(n)]
for i in range(m):
  a, b = map(int, input().split())
  matrix[a-1][b-1] = 1
  matrix[b-1][a-1] = 1

used = [False]*n
used[0] = True

print(dfs(0, used))
