import math
t=int(input())
for you in range(t):
    l=input().split()
    a=int(l[0])
    b=int(l[1])
    if(a>b):
        a,b=b,a
    if(b%a!=0):
        print(-1)
    else:
        z=b//a
        if(z&(z-1)):
            print(-1)
        else:
            pow=0
            while(z>0):
                z=z//2
                pow+=1
            pow=pow-1
            print(math.ceil(pow/3))

