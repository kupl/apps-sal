N,K=map(int,input().split())
A=list(map(int, input().split()))
if N==K:
    print(1)
    return
else:
    a,mod=divmod(N-1,K-1)
    if mod==0:
        print(a)
    else:
        print(a+1)
