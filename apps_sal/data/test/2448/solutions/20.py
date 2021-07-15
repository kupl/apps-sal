import sys
t=int(sys.stdin.readline())
# t=1
for i in range(t):
    n=int(sys.stdin.readline())
    a,b,c=list(map(int,sys.stdin.readline().strip().split()))
    x=list(sys.stdin.readline())
    op=[' ']*n
    # print(op)
    # print(x)
    
    if(n%2==0):
        w=n//2
    else:
        w=n//2+1
        
    z=0
    for j in range(n):
        if(x[j]=='R'):
            if(b>0):
                b-=1
                z+=1
                op[j]='P'
        elif(x[j]=='S'):
            if(a>0):
                a-=1
                z+=1
                op[j]='R'
        elif(x[j]=='P'):
            if(c>0):
                c-=1
                z+=1
                op[j]='S'
    for j in range(n):
        if(op[j]==' '):
            if(a>0):
                a-=1
                op[j]='R'
            elif(b>0):
                op[j]='P'
                b-=1
            elif(c>0):
                op[j]='S'
                c-=1
    if(z>=w):
        print("YES")
        print("".join(op))
    else:
        print("NO")
