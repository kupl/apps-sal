N,K,M=map(int, input().split())
A=map(int,input().split())

x=M*N-sum(A)

if K>=x:
    if x<=0:
        print(0)
    else:
        print(x)

else:
    print(-1)
