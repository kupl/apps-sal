from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

a,b=nii()

num=1
ans=0
while num<b:
  ans+=1
  num+=a-1

print(ans)
