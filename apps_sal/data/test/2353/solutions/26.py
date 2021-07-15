import math
t=int(input())
for you in range(t):
    l=input().split()
    a=int(l[0])
    b=int(l[1])
    c=int(l[2])
    d=int(l[3])
    if(b>=a):
        print(b)
    else:
        rem=(a-b)
        time=b
        if(d>=c):
            print(-1)
        else:
            x=math.ceil(rem/(c-d))
            time+=(x*c)
            print(time)

