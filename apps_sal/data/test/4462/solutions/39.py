n=int(input())
a=list(map(int,input().split()))

x2=0
x4=0
x1=0
for x in a:
  if x%2==0:
    x2+=1
  if x%4==0:
    x4+=1
  if x%2==1:
    x1+=1
    
if x4+x1==n:
  if x4>=x1-1:
    print('Yes')
  else:
    print('No')
  
else:
  if x4>=x1:
    print('Yes')
  else:
    
    print('No')

