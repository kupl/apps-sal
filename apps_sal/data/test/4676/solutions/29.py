o=input()
e=input()
n=len(o)
m=len(e)
ans=[]
for i in range(m):
  ans.append(o[i])
  ans.append(e[i])
if n-m==0:
  print(*ans,sep='')
else:
  ans.append(o[n-1])
  print(*ans,sep='')
