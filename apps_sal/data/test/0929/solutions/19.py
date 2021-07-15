H,W=list(map(int,input().split()))
a=[list(map(int,input().split())) for i in range(H)]
cells=[]
for i in range(H):
    if i%2==0:
        for j in range(W):
            cells.append((i,j))
    else:
        for j in range(W-1,-1,-1):
            cells.append((i,j))
ans=[]
for k in range(H*W-1):
    i,j=cells[k]
    if a[i][j]%2==1:
        ni,nj=cells[k+1]
        a[i][j]-=1
        a[ni][nj]+=1
        ans.append([i+1,j+1,ni+1,nj+1])
print((len(ans)))
for i in range(len(ans)):
    print((ans[i][0],ans[i][1],ans[i][2],ans[i][3]))

