n,m,k=list(map(int,input().split()))
ar=[]
tr=[[1,1],[-1,1],[-1,-1],[1,-1]]
for x in range(n):
    ar.append([0]*m)
for v in range(k):
    c,d=list(map(int,input().split()))
    c+=-1
    d+=-1
    ar[c][d]=1
    for x in tr:
        if c+x[0]<n and c+x[0]>=0 and d+x[1]<m and d+x[1]>=0:
            if ar[c][d+x[1]]==1 and ar[c+x[0]][d]==1 and ar[c+x[0]][d+x[1]]==1:
                print(v+1)
                return
print(0)

