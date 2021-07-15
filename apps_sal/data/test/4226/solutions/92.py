X,Y = map(int,input().split())
flg = 0
for i in range(X+1):
  if(i*2+(X-i)*4==Y):
    flg=1
    
if(flg==1):
  print('Yes')
else:
  print('No')
