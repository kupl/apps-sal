import sys
y,x=list(map(int,input().split()))
if ((x==1 and y>0 )or (x==0 )or (x>1 and y==0) or(y<x-1)):
    print('No')
    return
if (x%2==1 and y%2==0)or(x%2==0 and y%2==1):
    print('Yes')
else:
    print('No')

