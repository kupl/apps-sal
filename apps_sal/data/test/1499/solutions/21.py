n, m = [int(c) for c in input().split()]
for i in range(1, 2 * n, 2):
    for j in (2 * n + i, i, 2 * n + i + 1, i + 1):
        if j <= m:
            print(j, end=' ')
