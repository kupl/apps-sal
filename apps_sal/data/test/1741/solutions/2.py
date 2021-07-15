def bs(x,y,n,p):
        r=0
        for i in range(n):
                 #z= (0.5*((x[i]-p)**2 +(y[i])**2))/y[i]
                  z=(p-x[i])*(p-x[i]) + 1.0*y[i]*y[i]
                  z=z/2.0
                  z=z/y[i]
                  z=abs(z)
                  r=max(z,r)
        return r
        

n=int(input())
y=[]
x=[]
k=z=0
for i in range(n):
        a,b=[int(i) for i in input().split()]
        if b>0:
                k=1
        if b<0:
                z=1
        x.append(a)
        y.append(b)
if k==1 and z==1:
        print(-1)
else:
        z=120
        l=min(x)
        rt=max(x)
        while(z):
                #p1=(rt+2*l)/3
                #p2=(l+2*rt)/3
                p1=(2*l+rt)/3
                p2=(2*rt+l)/3
                if bs(x,y,n,p1)<bs(x,y,n,p2):
                        #rt=p2
                        rt=p2
                else:
                        l=p1
                z=z-1
        print(bs(x,y,n,l))
                        

