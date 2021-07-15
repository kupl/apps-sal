n,m=map(int,input().split())
sc=[list(map(int,input().split())) for i in range(m)]
ans=[-1]*(n)
flag=True

for i in sc:
  if ans[i[0]-1]==-1:
    ans[i[0]-1]=i[1]
  elif ans[i[0]-1]!=-1 and ans[i[0]-1]!=i[1]:
    flag=False
    break
for i in range(n):
  if i==0 and ans[i]==-1:
    if n==1:
      ans[i]=0
    else:
      ans[i]=1
  elif ans[i]==-1:
    ans[i]=0
if flag and (ans[0]!=0 or n==1):
  print("".join(map(str,ans)))
else:
  print(-1)
