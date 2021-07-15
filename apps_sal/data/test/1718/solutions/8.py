N,K=map(int,input().split())
A=list(map(int, input().split()))

a,mod=divmod(N-1,K-1)
if mod==0:
    print(a)
else:
    print(a+1)
