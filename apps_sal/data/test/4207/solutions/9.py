n=int(input().strip())
from fractions import gcd
a=list(map(int,input().strip().split(" ")))
b=list(map(int,input().strip().split(" ")))
d={}
t=0
for i in range(0,len(a)):
    if( b[i]==0 and a[i]!=0):
        if("x" not in d.keys()):
            d["x"]=1
        else:
            d["x"]+=1
    elif (a[i] == 0  and b[i]==0 ):
        d["m"]=0
        t+=1
    elif(a[i]==0 and b[i]!=0):
        d["y"]=0
    else:
        p=gcd(a[i],b[i])
        x=a[i]//p
        y=b[i]//p
        if(y<0):
            y=-y
            x=-x
        if ((x,y) not in d.keys()):
            d[(x,y)] = 1
        else:
            d[(x,y)] += 1
print(max(d.values())+t)
