(n, m) = map(int, input().split())
ab = list((list(map(int, input().split())) for _ in range(n)))
cd = list((list(map(int, input().split())) for _ in range(m)))
for j in range(n):
    (a, b) = (ab[j][0], ab[j][1])
    (ans, res) = (0, 1001001001)
    for i in range(m):
        (c, d) = (cd[i][0], cd[i][1])
        if abs(a - c) + abs(b - d) < res:
            res = abs(a - c) + abs(b - d)
            ans = i + 1
    print(ans)
