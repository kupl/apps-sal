n,q=list(map(int,input().split()))
a=list(map(int,input().split()))
x=max(a)
y=min(a)
for i in range(q):
 p=int(input())
 if p<=x and p>=y:
  print('Yes')
 else:
  print('No')

