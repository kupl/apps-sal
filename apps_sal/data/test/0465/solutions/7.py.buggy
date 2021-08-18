n, a, b = map(int, input().split())
if (n == 3 or n == 2) and (a == 1 and b == 1):
    print("NO")
    return
g = [[0 for i in range(n)] for j in range(n)]
if a > 1 and b == 1:
    for i in range(n - a - 1, -1, -1):
        g[i][i + 1] = g[i + 1][i] = 1
elif b > 1 and a == 1:
    a, b = b, a
    for i in range(n - a - 1, -1, -1):
        g[i][i + 1] = g[i + 1][i] = 1
    for i in range(n):
        for j in range(n):
            if g[i][j] == 0:
                g[i][j] = 1
            elif g[i][j] == 1:
                g[i][j] = 0
    for i in range(n):
        g[i][i] = 0
elif a == 1 and b == 1:
    for i in range(n - 1):
        g[i][i + 1] = g[i + 1][i] = 1
elif a > 1 and b > 1:
    print("NO")
    return
print("YES")
for i in range(n):
    for j in range(n):
        print(g[i][j], end='')
    print()
