n, m = map(int, input().split())
e = [[0] * n for i in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    e[a - 1][b - 1] += c
    e[b - 1][a - 1] -= c
cnt = 0
for i in range(n):
    cnt1 = 0
    for j in range(n):
        cnt1 += e[i][j]
    cnt += abs(cnt1)
print(cnt // 2)
