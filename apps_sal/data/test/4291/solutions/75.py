N,Q=map(int,input().split())
S=input()
B=[0]*N
for i in range(1,N):
    if S[i-1]=='A' and S[i]=='C':
        B[i]=B[i-1]+1
    else:
        B[i]=B[i-1]
for i in range(Q):
    l,r=map(int,input().split())
    print(B[r-1]-B[l-1])
