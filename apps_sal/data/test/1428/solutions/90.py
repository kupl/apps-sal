n,c = map(int,input().split())
d = [list(map(int,input().split())) for i in range(c)]
l = [list(map(int,input().split())) for i in range(n)]

ll = [[0]*c for i in range(3)]

for i in range(n):
    for j in range(n):
        x = (i+j+2)%3
        ll[x][l[i][j]-1] += 1

ans = float("INF")

for i in range(c):
    for j in range(c):
        if i == j:
            continue
        for k in range(c):
            if i == k or j == k:
                continue
            count = 0
            ch = [i,j,k]
            for m in range(3):
                for t in range(c):
                    count += ll[m][t]*d[t][ch[m]]
            ans = min(ans,count)
print(ans)
