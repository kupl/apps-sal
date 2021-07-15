N,K,Q=list(map(int,input().split()))
A=[int(input()) for _ in range(Q)]
a=[K]*N
for i in range(Q):
    a[A[i]-1]+=1
for i in range(N):
    if a[i]-Q>0:
        print('Yes')
    else:
        print('No')

