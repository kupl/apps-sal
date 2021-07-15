A, B, C, X, Y = map(int,input().split())
ans = float('inf')
for i in range(0, max(X,Y)+1):
  num = i*2*C + max(0, X-i)*A + max(0, Y-i)*B
  ans = min(ans, num)
print(ans)
