(n, m) = map(int, input().split())
data = [[] for i in range(n)]
data2 = [[0] * n for i in range(m)]
for i in range(n):
    data[i] = list(map(int, input().split()))
a = 0
for i in range(m):
    for j in range(n):
        data2[i][j] = data[j][i]
for i in range(n):
    su = sum(data[i])
    if su != 0:
        a += 2 ** su - 1
    if m - su != 0:
        a += 2 ** (m - su) - 1
for i in range(m):
    su = sum(data2[i])
    if su != 0:
        a += 2 ** su - 1
    if n - su != 0:
        a += 2 ** (n - su) - 1
print(a - n * m)
