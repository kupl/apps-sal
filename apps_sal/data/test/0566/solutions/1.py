x,y,z=list(map(int,input().split()))
L=[x,y,z]
L.sort()
x=L[2]
y=L[1]
z=L[0]
n=2*y+2*z
a=-1
b=y+z+1
while(b-a>1):
    e=(b+a)//2
    if(n-2*e<=x+e):
        b=e
    else:
        a=e

print(min((n-2*b)//2,(x+b)//2))

