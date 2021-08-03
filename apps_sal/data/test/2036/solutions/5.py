mod = 10**9 + 7
n, m, x, y = map(int, input().split())
for i in range(y, m + 1):
    print(x, i)
for i in range(y - 1, 0, -1):
    print(x, i)
ch = 0
for i in range(x + 1, n + 1):
    if ch == 0:
        for j in range(1, m + 1):
            print(i, j)
    else:
        for j in range(m, 0, -1):
            print(i, j)
    ch = 1 - ch
for i in range(x - 1, 0, -1):
    if ch == 0:
        for j in range(1, m + 1):
            print(i, j)
    else:
        for j in range(m, 0, -1):
            print(i, j)
    ch = 1 - ch
