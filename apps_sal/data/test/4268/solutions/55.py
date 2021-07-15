n,d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n-1):
  for j in range(i+1, n):
    t = 0
    for k in range(d): t += abs(x[i][k] - x[j][k])**2
    t **= 0.5
    if t.is_integer(): ans += 1
print(ans)
