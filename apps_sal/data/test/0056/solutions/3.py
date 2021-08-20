(n, t) = map(int, input().split())
a = [[None]] + [[0] * i for i in range(1, n + 1)]
c = 2 ** (n + 1)
for _ in range(t):
    a[1][0] += c
    for i in range(1, n + 1):
        for j in range(i):
            if a[i][j] > c:
                diff = a[i][j] - c
                a[i][j] = c
                if i < n:
                    a[i + 1][j] += diff // 2
                    a[i + 1][j + 1] += diff // 2
full = 0
for i in range(1, n + 1):
    for j in range(i):
        full += a[i][j] == c
print(full)
