A, B, C, X, Y = map(int, input().split())
ans = float('INF')
for k in range(0, 2*max(X, Y)+1, 2):
  i = max(0, X - int(k/2))
  j = max(0, Y - int(k/2))
  ans = min(ans, A*i + B*j + C*k)
print(ans)
