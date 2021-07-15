x=[]

for i in range(3):
    a=list(map(int,input().split()))
    x.append(a)

def ok(a,b,n):
    nonlocal x
    return x[n][0]<=a<=x[n][2] and x[n][1]<=b<=x[n][3]

#a[0][0] a[0][1] : a[0][0] a[0][3] : a

def kol(n):
    nonlocal x
    t=0
    x1=x[0][0]
    y1=x[0][1]
    x2=x[0][2]
    y2=x[0][3]
    if ok(x1,y1,n): t+=1
    if ok(x1,y2,n): t+=1
    if ok(x2,y1,n): t+=1
    if ok(x2,y2,n): t+=1
    return t
k1=kol(1)
k2=kol(2)

def ooo():
    x1=x[0][0]
    y1=x[0][1]
    x2=x[0][2]
    y2=x[0][3]
    t=True
    t=t and (ok(x1,y1,1) or ok(x1,y1,2))
    t=t and (ok(x1,y2,1) or ok(x1,y2,2))
    t=t and (ok(x2,y1,1) or ok(x2,y1,2))
    t=t and (ok(x2,y2,1) or ok(x2,y2,2))
    return t

    
if k1==4 or k2==4:
    print('NO')
elif k1+k2<4:
    print('YES')
elif not ooo():
    print('YES')
else:
    x1=x[0][0]
    y1=x[0][1]
    x2=x[0][2]
    y2=x[0][3]
    if ok(x1,y1,2):
        x[1],x[2]=x[2],x[1]
    if ok(x2,y1,1):
        if x[1][3]>=x[2][1]:
            print('NO')
        else: print('YES')
    else:
        if x[1][2]>=x[2][0]:
            print('NO')
        else: print('YES')

