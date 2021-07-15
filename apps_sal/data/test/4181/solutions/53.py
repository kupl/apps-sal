n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))+[0]
ans=0
for i in range(n+1):
  if a[i]>=b[i]:
    ans+=b[i]
  else:
    ans+=a[i]
    d=b[i]-a[i]
    if a[i+1]>d:
      ans+=d
      a[i+1]-=d
    else:
      ans+=a[i+1]
      a[i+1]=0
print(ans)
