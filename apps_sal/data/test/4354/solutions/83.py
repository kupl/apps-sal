(n, m) = list(map(int, input().split()))
ab = [tuple(map(int, input().split())) for _ in range(n)]
cd = [tuple(map(int, input().split())) for _ in range(m)]
for i in range(n):
    x = 1 << 30
    y = -1
    (a, b) = ab[i]
    for j in range(m):
        (c, d) = cd[j]
        d = abs(a - c) + abs(b - d)
        if x > d:
            x = d
            y = j
    print(y + 1)
