Q=int(input())
lr=[list(map(int,input().split()))for _ in range(Q)]

N=10**5
A=[1]*(N+1)
A[0]=A[1]=0
i=2
while i*2<=N:
    if A[i]:
        j=2
        while i*j<=N:
            A[i*j]=0
            j+=1
    i+=1

S=[0]*(N+1)
for i in range(N+1):
    if A[i] and A[(i+1)//2]:
        S[i]=1
    S[i]+=S[i-1]

for l,r in lr:
    print(S[r]-S[l-1])
