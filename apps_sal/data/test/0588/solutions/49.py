import numpy as np

n=int(input())

def div2(x,y):
    if x>0:
        return (1,y/x)
    elif x<0:
        return (-1,y/x)
    else:
        if y>0:
            return (-1,-float("inf"))
        else:
            return (1,-float("inf"))
    

L=[list(map(int,input().split())) for i in range(n)]

L.sort(key=lambda x:div2(x[0],x[1]))

m=0
for i in range(n):
    for j in range(i,n):
        x0=y0=0
        x1=y1=0
        for k in range(n):
            if i<=k<=j:
                x0+=L[k][0]
                y0+=L[k][1]
            else:
                x1+=L[k][0]
                y1+=L[k][1]
        m=max(m,x0**2+y0**2,x1**2+y1**2)

print('{:.12f}'.format(np.sqrt(m)))
