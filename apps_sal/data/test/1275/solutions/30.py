n,k = map(int,input().split())
k = abs(k)
x = 0
for i in range(2+k,2*n+1):
  y = i-1 if i<=n+1 else 2*n-i+1
  z = i-k-1 if i<=n+k+1 else 2*n-i+k+1
  x += y*z
print(x)
