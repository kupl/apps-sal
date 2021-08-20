(n, m, h) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [list(map(int, input().split())) for _ in range(n)]
d = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if c[i][j]:
            d[i][j] = min(a[j], b[i])
for i in d:
    print(*i)
