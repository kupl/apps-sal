N,K=list(map(int,input().split()))
if K%2==0:
    x=N//(K//2)
    print(((x-x//2)**3+(x//2)**3))
else:
    print(((N//K)**3))

