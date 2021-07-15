q,w,e=list(map(int,input().split()))
if e%2==1:
    c='L'
else:
    c='R'
e=(e+1)//2
x=e%w
if x==0:
    x=w
if e%w==0:
    z=e//w
else:
    z=e//w+1
print(z,x,c)

