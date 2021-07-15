n,q,c = list(map(int,input().split()))
sky = [[[0] * 11 for j in range(101)] for i in range(101)]
c += 1
for i in range(n):
    x,y,s = list(map(int,input().split()))
    sky[y][x][s % c] += 1

for k in range(11):
    i = 1
    while i < 101:
        j = 1
        while j < 101:
            sky[i][j][k] += (sky[i-1][j][k]  + sky[i][j-1][k] -  sky[i-1][j-1][k])
            j += 1
        i += 1
req = [list(map(int,input().split())) for i in range(q)]
for i in range(q):
    t,x,y,x2,y2 = req[i]
    ans = 0
    j = 0
    while j < c:
        ans += (sky[y2][x2][j] - sky[y2][x-1][j] - sky[y-1][x2][j] + sky[y-1][x-1][j]) * ((j + t) % c)
        j += 1
    print(ans)

