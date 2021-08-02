n, m, h = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))
l = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        l[i][j] = min(a[j], b[i])
for i in range(n):
    p = list(map(int, input().split()))
    for j in range(m):
        if p[j] == 0:
            l[i][j] = 0
for i in l:
    print(*i)
