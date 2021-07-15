def mp():
    return map(int, input().split())

def f(i, j):
    return a[i][j] == a[i + 1][j] == a[i][j + 1] == a[i + 1][j + 1] == 1

n, m = mp()
a = [list(mp()) for i in range(n)]
b = [[0] * m for i in range(n)]

ans = []
for i in range(n - 1):
    for j in range(m - 1):
        if f(i, j):
            ans.append((i + 1, j + 1))
            b[i][j] = 1
            b[i][j + 1] = 1
            b[i + 1][j] = 1
            b[i + 1][j + 1] = 1

fail = False
for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            fail = True

if fail:
    print(-1)
else:
    print(len(ans))
    for i in ans:
        print(*i)
