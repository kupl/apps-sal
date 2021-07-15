n=int(input())
a=[list(map(int,input().split())) for i in range(2)]
ans=0
if n==1:
  print(sum(a[0])+sum(a[1]))
  return
for i in range(n):
  ans=max(ans,sum(a[0][0:i])+sum(a[1][i-1:n]))
print(ans)
