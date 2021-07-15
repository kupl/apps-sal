a,b,c,n=list(map(int,input().split()))
if (c > a or c > b or a + b - c > n - 1):
  print(-1)
else:
  print(n-a-b+c)

