N,M,X=map(int,input().split())
L=[list(map(int,input().split())) for i in range(N)]
a=2**N
J=[]
for i in range(a):
    T=True
    K=[0]*(M+1)
    for j in range(N):
        if (i>>j)&1:
            for k in range(M+1):
                K[k]+=L[j][k]
    for j in range(1,M+1):
        if K[j]<X:
            T=False
    if T:
        J.append(K[0])
if len(J)==0:
    print(-1)
else:
    J.sort()
    print(J[0])
