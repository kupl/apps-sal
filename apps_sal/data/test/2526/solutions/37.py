from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

x,y,a,b,c=nii()
p=sorted(lnii(),reverse=True)
q=sorted(lnii(),reverse=True)
r=sorted(lnii(),reverse=True)

l=p[:x]+q[:y]
l.sort()

ans=0
for i in range(x+y):
  if i<c:
    ans+=max(l[i],r[i])
  else:
    ans+=l[i]

print(ans)
