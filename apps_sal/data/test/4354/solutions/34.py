(n, m) = map(int, input().split())
ab = [list(map(int, input().split())) for p in range(n)]
cd = [list(map(int, input().split())) for q in range(m)]
for i in range(n):
    x = 10 ** 10
    ans = 0
    for j in range(m):
        if abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1]) < x:
            ans = j + 1
            x = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
    print(ans)
