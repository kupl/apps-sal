a=int(input())
lis=list(map(int,input().split()))
ans=0
for i in range(a-1):
  if lis[i]>lis[i+1]:
    j=lis[i]-lis[i+1]
    ans+=j
    lis[i+1]=lis[i]
print(ans)
