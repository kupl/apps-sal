ans=10**10
n=int(input())
a=list(map(int,input().split()))
for i in range(-100,101):
  x=0
  for j in range(n):
    x+=(i-a[j])**2
  ans=min(x,ans)
print(ans)
