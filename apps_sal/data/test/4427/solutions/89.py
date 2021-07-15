r,d,x=map(int,input().split())
ans =  x
for i in range(10):
  ans = r*ans-d
  print(ans)
