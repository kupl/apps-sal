import sys
read=sys.stdin.read

n,*p=map(int,read().split())
p.append(-1)
cl=[]
f=0
for i in range(n+1):
  if p[i]==i+1:
    if f==0:
      cl.append(1)
      f=1
    else:
      cl[-1]+=1
  else:
    if f==1:
      cl[-1]=cl[-1]//2+(cl[-1]%2)
    f=0

print(sum(cl))
