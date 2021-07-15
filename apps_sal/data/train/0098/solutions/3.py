t = int(input())
for i in range(t):
  c,m,x = map(int,input().split())
  ans1 = min(c,m)
  ans2 = (c+m+x)//3
  print(min(ans1,ans2))
