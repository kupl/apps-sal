n,m=[int(x) for x in input().split()]
t=[int(x) for x in input().split()]
p=min(t)
q=max(t)
for i in range(m):
 r=int(input())
 if r>=p and r<=q:
  print('Yes')
 else:
  print('No')
