from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n,m=nii()
l=[lnii() for i in range(m)]

for i in range(1000):
  num=str(i)
  judge=True
  for j in range(m):
    s,c=l[j]
    s-=1
    c=str(c)
    if s>=len(num) or num[s]!=c:
      judge=False

  if judge and len(num)==n:
    print(i)
    return

print(-1)
