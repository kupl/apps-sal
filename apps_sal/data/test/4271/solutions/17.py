n=int(input())
a=list(map(lambda x:int(x)-1, input().split()))
ans=sum(list(map(int,input().split())))
c=list(map(int,input().split()))

for i in range(n-1):
  if a[i]+1==a[i+1]:
    ans+=c[a[i]]

print(ans)
