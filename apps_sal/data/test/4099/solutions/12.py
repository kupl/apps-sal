n,k,m=map(int,input().split())
a=list(map(int,input().split()))
if sum(a)+k<n*m:
    print(-1)
else:
    for i in range(k+1):
        if sum(a)+i>n*m:
            print(0)
            break
        if sum(a)+i==n*m:
            print(i)
            break
