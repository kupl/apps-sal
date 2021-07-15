q=int(input())
LR=[map(int, input().split()) for _ in range(q)]
L,R=[list(i) for i in zip(*LR)]

import math

N=100000

A=[] #素数なら1,素数でなければ0
for i in range(N+1):
    A.append(1)

A[0]=0
A[1]=0

i=2
while i<=math.sqrt(N):
    if A[i]==0:
        i+=1
        continue
    j=2
    while i*j<=N:
        A[i*j]=0
        j+=1
    i+=1

S=[] #「2017に似た数」なら1,「2017に似た数」でなければ0
for i in range(N+1):
    S.append(0)
for x in range(1,N,2):
    if A[x]==1 and A[(x+1)//2]==1:
        S[x]=1

T=[0] #Sの累積和
for y in range(N+1):
    T.append(T[y]+S[y])
del T[0]

for z in range(q):
    ans=T[R[z]]-T[L[z]-1]
    print(ans)
