rw = int(input())
for wewq in range(rw):
    (n, m) = list(map(int, input().split()))
    a = [0] * n
    f = 0
    for i in range(n):
        a[i] = list(map(int, input().split()))
    for i in range((n + 1) // 2):
        for j in range((m + 1) // 2):
            if j > m // 2 - 1 or i > n // 2 - 1:
                b = [a[i][j], a[n - i - 1][m - j - 1]]
                f += abs(b[1] - b[0])
                continue
            b = [a[i][j], a[n - i - 1][j], a[i][m - j - 1], a[n - i - 1][m - j - 1]]
            c = []
            c.append(abs(b[0] - b[1]) + abs(b[0] - b[2]) + abs(b[0] - b[3]))
            c.append(abs(b[1] - b[0]) + abs(b[1] - b[2]) + abs(b[1] - b[3]))
            c.append(abs(b[2] - b[1]) + abs(b[2] - b[0]) + abs(b[2] - b[3]))
            c.append(abs(b[3] - b[1]) + abs(b[3] - b[2]) + abs(b[3] - b[0]))
            f += min(c)
    print(f)
