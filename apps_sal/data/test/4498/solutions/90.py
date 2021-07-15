from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

a,b,c,d=nii()
if (abs(a-b)<=d and abs(c-b)<=d) or abs(c-a)<=d:
  print('Yes')
else:
  print('No')
