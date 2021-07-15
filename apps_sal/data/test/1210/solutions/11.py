n,p=list(map(int,input().split()))
z=1
a=[]
b=[]
for i in range(0,n):
    x,y=list(map(int,input().split()))
    a.append(int(y/p)-int((x-1)/p))
    b.append(y-x+1)
ans=0
for i in range (0,n):
    pz=a[(i+1)%n]
    z=b[(i+1)%n]
    py=a[i]
    y=b[i]
    px=a[(i-1+n)%n]
    x=b[(i-1+n)%n]
    ans+=((x*z*py*2000 + px*pz*(y-py)*2000 + px*(y-py)*(z-pz)*1000 + pz*(x-px)*(y-py)*1000))/float(x*y*z)
    
    
    
print(ans)


