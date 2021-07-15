n=int(input())
a=list(map(int,input().split()))
count=0
ans=1
color_lis=[0,0,0,0,0,0,0,0]
for i in range(n):
  if a[i]//400>=8:
    count+=1
  else:
    color_lis[a[i]//400]=1
ans=sum(color_lis)
if count>0:
  flag=1
else:
  flag=0
ans1 = max(flag,ans)
ans2 = ans+count
print(ans1,ans2)
