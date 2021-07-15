n , c = list(map(int,input().split()))
iwaka = [list(map(int,input().split())) for i in range(c)]
masu = [list(map(int,input().split())) for i in range(n)]
amari = [{} for i in range(3)]

for i in range(n):
    for j in range(n):
        amari[(i+j)%3][masu[i][j]] = amari[(i+j)%3].get(masu[i][j],0) + 1

kouho = []
for i in range(c):
    for j in range(c):
        for k in range(c):
            if i != j and j != k and k != i:
                kouho.append((i+1,j+1,k+1))
ans = 10**9
for p in kouho:
    cou = 0
    for i in range(3):
        for k , v in list(amari[i].items()):
            cou += iwaka[k-1][p[i]-1]*v
    ans = min(ans,cou)
print(ans)

