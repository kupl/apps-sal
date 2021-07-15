import math
def Q(x,y):
    if(x==0):
        if(y>0):
            return math.pi/2
        if(y<0):
            return (math.pi/2)*3
    #y=mx
    m=abs(y/x)
    theta=math.atan(m)
    if(y>=0 and x>=0):
        return theta
    if(y>=0 and x<=0):
        return math.pi-theta
    if(y<=0 and x<=0):
        return math.pi+theta
    else:
        return 2*math.pi-theta
    

n=int(input())
P=[]
for i in range(n):
    x,y=list(map(int,input().split()))
    P.append(Q(x,y))

P.sort()
ans=360
for i in range(1,n):
    ans=min(ans,(math.pi*2)-(P[i]-P[i-1]))
ans=min(ans,P[n-1]-P[0])
print((ans*360)/(2*math.pi))

