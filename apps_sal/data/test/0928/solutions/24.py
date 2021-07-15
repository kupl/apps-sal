from itertools import accumulate
N,K=map(int,input().split())
A=list(map(int,input().split()))
A_=[0]+list(accumulate(A))

N_=N+1
x=0
ans=0
for i in range(N_):
    S=A_[i]-A_[x]
    if S>=K:
        while (S>=K and x!=i):
            ans+=N_-i
            x+=1
            S=A_[i]-A_[x]
print(ans)
