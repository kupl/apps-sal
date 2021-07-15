n,m,q = map(int,input().split())
bi = [[0 for i in range(n+1)] for j in range(n+1)]
for i in range(m):
    l,r = map(int,input().split())
    bi[l][r] += 1
ans = [[0 for i in range(n+1)] for j in range(n+1)]
for i in range(1,n+1):
    cou = 0
    for j in range(1,n+1):
        cou += bi[i][j]
        ans[i][j] = ans[i-1][j] + cou

for i in range(q):
    p , q  =map(int,input().split())
    print(ans[q][q]-ans[q][p-1]-ans[p-1][q]+ans[p-1][p-1])
