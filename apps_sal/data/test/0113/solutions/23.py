q,w=list(map(int,input().split()))
z,x=0,0
e=q
while e%5==0:
    z+=1
    e//=5
while e%2==0:
    x+=1
    e//=2
if w>z:
    z=w-z
else:
    z=0
if w>x:
    x=w-x
else:
    x=0
print(q*(5**z)*(2**x))

