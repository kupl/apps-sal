import sys
n,q=map(int,sys.stdin.readline().split())
n1=n%2
n2=n//2
n3=(n*n+1)//2
for i in range(q):
    x,y=map(int,sys.stdin.readline().split())
    if n1==0:
        if (x+y)%2==0:
            print((x-1)*n2+(y-1)//2+1) 
        else:
            print(n3+(x-1)*n2+(y-1)//2+1)
    else:
        if (x+y)%2==0:
            print(((x-1)*n+1)//2+(y-1)//2+1) 
        else:
            print(n3+(((x-1)*n)//2)+(y-1)//2+1)
