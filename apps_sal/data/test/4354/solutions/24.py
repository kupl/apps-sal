n, m = list(map(int, input().split()))
al = [list(map(int, input().split())) for _ in range(n)]
cl = [list(map(int, input().split())) for _ in range(m)]

for a in al:
    ans, dis = 0, 1001001001
    for i in range(m):
        _dis = abs(a[0]-cl[i][0]) + abs(a[1]-cl[i][1])
        if _dis < dis:
            ans, dis = i+1, _dis
    print(ans)

