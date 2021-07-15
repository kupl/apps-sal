N,K,C=map(int,input().split())
S=input()
i=0
d1=[-1]*N
for k in range(K):
    while S[i]=='x' and i<N:
        i+=1
    if i==N:break
    d1[i]=k
    i+=C+1
i=0
d2=[-1]*N
for k in range(K-1,-1,-1):
    while S[N-1-i]=='x' and i<N:
        i+=1
    if i==N:break
    d2[N-1-i]=k
    i+=C+1
print(*[i+1 for i in range(N) if d1[i]==d2[i]>=0],sep='\n')
