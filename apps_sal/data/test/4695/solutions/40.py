a=[1,3,5,7,8,10,12]
b=[4,6,9,11]
c=[2]
p=0
q=0

s=list(map(int,input().split()))

for i in a:
  if s[0]==i:
    p=0
  elif s[0]==2:
    p=2
  else:
    p=1

for i in a:
  if s[1]==i:
    q=0
  elif s[1]==2:
    q=2
  else:
    q=1

if p==q:
  print('Yes')
else:
  print('No')

