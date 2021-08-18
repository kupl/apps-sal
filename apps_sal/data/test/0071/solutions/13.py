import sys

n, m, k, x, y = map(int, input().split())

if n == 1:
    max_q = k // m + (k % m != 0)
    min_q = k // m
    serg_q = k // m + (y <= k % m)
    pass
else:
    num_q = [[0] * m for i in range(n)]

    loop = k // ((2 * n - 2) * m)

    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1:
                num_q[i][j] = loop
            else:
                num_q[i][j] = 2 * loop

    amari = k % ((2 * n - 2) * m)
    zenhan = min((n - 1) * m, amari)
    kouhan = max(amari - (n - 1) * m, 0)

    for i in range(zenhan):
        num_q[i // m][i % m] += 1

    for i in range(kouhan):
        num_q[(n - 1) - (i // m)][i % m] += 1

    max_q = -1
    min_q = float('inf')

    for i in range(n):
        max_q = max(max_q, max(num_q[i]))
        min_q = min(min_q, min(num_q[i]))

    serg_q = num_q[x - 1][y - 1]

    pass

print(max_q, min_q, serg_q)
