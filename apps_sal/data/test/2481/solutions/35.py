H,W=map(int,input().split())
C=[list(map(int,input().split()))for _ in range(10)]
A=[list(map(int,input().split()))for _ in range(H)]

for k in range(10):#経由する頂点
    for i in range(10):#始点
        for j in range(10):#終点
            C[i][j] = min(C[i][j], C[i][k] + C[k][j])
ans=0
for aa in A:
    for a in aa:
        if a==-1:
            ans+=0
        else:
            ans+=C[a][1]
print(ans)
