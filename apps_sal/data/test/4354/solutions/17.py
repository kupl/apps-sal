(n, m) = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
b = [list(map(int, input().split())) for i in range(m)]
for i in range(n):
    c = float('inf')
    e = 0
    g = 0
    for j in range(m):
        d = abs(a[i][0] - b[j][0]) + abs(a[i][1] - b[j][1])
        g += 1
        if d < c:
            (c, e) = (d, g)
    print(e)
