from math import gcd as gcd
n,a,b=list(map(int,input().split()))
ma=max(a,b)
mi=min(a,b)
t=1
if n%gcd(a,b)!=0:
    print(-1)
else:
    ab=[0]*(n+1)
    for i in range(0,10**6 + 1):
        if (n-ma*i)%mi==0 and (n-ma*i)//mi>=0:
            x=i
            y=(n-ma*i)//mi
            t=0
            break
    if t:
        print(-1)
    else:
            
        # print(x,y)
        ind=0
        for i in range(x):
            for j in range(ma*i + 1,(ma)*(i+1) + 1):
                # print(j)
                if j>1000000:
                    print(j)
                ab[j]=(j+1)
                if j%ma==0:
                    ab[j]=(j-ma) + 1
                # print(ab)    
        k=ma*x
        for i in range(y):
            for j in range(mi*i + 1,(mi)*(i+1) + 1):
                ab[k+j]=(k+j+1)
                if j%mi==0:
                    ab[k+j]=(k+j-mi) + 1
                
        print(*ab[1:])            
                    
                

