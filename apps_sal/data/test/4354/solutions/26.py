n, m = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n)]
cd = [list(map(int, input().split())) for i in range(m)]
for i in range(n):
    Min = 4 * (10**8) + 1
    for j in range(m):
        d = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
        # print(d,ab[i][0],cd[j][0])
        if Min > d:
            Min = d
            ans = j + 1
    print(ans)
