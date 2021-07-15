N,K=map(int,input().strip().split())

if K%2==1:
    print((N//K)**3)
else:
    a=N//K
    b=N//(K//2)
    print(a**3+(b-a)**3)
