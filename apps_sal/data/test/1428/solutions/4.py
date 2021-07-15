n,c=map(int,input().split())
D=[]
for i in range(c):
    D.append(list(map(int,input().split())))
C=[]
for i in range(n):
    C.append(list(map(int,input().split())))
    
A=[[0]*c for i in range(3)]
for i in range(n):
    for j in range(n):
        a=(i+j)%3
        A[a][C[i][j]-1]+=1

ans=10**100
for a0 in range(c):
    for a1 in range(c):
        for a2 in range(c):
            if a0==a1 or a1==a2 or a2==a0:
                continue
            cnt=0
            for i in range(c):
                cnt+=D[i][a0]*A[0][i]
                cnt+=D[i][a1]*A[1][i]
                cnt+=D[i][a2]*A[2][i]
            ans=min(cnt,ans)
print(ans)
