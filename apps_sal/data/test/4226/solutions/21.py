x,y=map(int,input().split())
i=0
while i<=x:
  if y==2*i+4*(x-i):
    print('Yes'); return;
  i+=1
print('No')
