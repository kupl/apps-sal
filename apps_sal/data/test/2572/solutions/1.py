for _ in range(int(input())):
    n, m = map(int, input().split())
    x = []
    for i in range(n):
        x.append([*map(int, input().split())])
    s = 0
    for i in range(n // 2):
        for j in range(m // 2):
            a, b, c, d = sorted([x[i][j], x[i][m - 1 - j], x[n - 1 - i][j], x[n - 1 - i][m - 1 - j]])
            s += d + c - b - a
    for i in range(n // 2, (n + 1) // 2):
        for j in range(m // 2):
            s += abs(x[i][j] - x[i][m - 1 - j])
    for j in range(m // 2, (m + 1) // 2):
        for i in range(n // 2):
            s += abs(x[i][j] - x[n - 1 - i][j])
    print(s)
