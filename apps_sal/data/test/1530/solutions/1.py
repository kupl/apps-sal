from bisect import *
n=int(input())
d,a=[(0,0)],[0]*n
for i,x in enumerate(map(int,input().split())):
    no=bisect(d,(x,0))-1
    l,y=d[no]
    a[i]=str(y)
    d[no:no+1]=[(l,x),(x,x)]
print(' '.join(a[1:]))
