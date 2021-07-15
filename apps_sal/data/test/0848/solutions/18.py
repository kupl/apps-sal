import math
n,k=list(map(int,input().split()))

if k>=math.ceil(n/2):
    print(-1)
else:
    print(n*k)
    for i in range(1,n-k+1):
        for j in range(i+1,i+k+1):
            print(i,j)

    x=i+1
    for i in range(x,n+1):
        c=0
        for j in range(i+1,n+1):
            print(i,j)
            c+=1
        j=1
        for j in range(1,k-c+1):
            print(i,j)
            j+=1

