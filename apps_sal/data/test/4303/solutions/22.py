n,k = map(int, input().split())
x = list(map(int, input().split()))
ans = abs(x[k-1]) + 2*abs(x[0])
for i in range (n-k+1):
  if x[i+k-1] <= 0:
    ans = min(ans, -x[i])
  elif x[i] >= 0:
    ans = min(ans, x[i+k-1])
  else:
    ans = min(ans, -2*x[i] + x[i+k-1], 2*x[i+k-1] - x[i])
print(ans)
