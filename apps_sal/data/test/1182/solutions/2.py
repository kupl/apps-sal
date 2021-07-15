r, c, n, k = [int(i) for i in input().split()]
a = [[0] * r for i in range(c)]
for i in range(n):
    x, y = [int(i) for i in input().split()]
    a[y - 1][x - 1] = 1
ct1 = 0
for i in range(c):
    for j in range(r):
        for s in range(i + 1, c + 1):
            for t in range(j + 1, r + 1):
                ct = 0
                for u in range(i, s):
                    for v in range(j, t):
                        if a[u][v] == 1:
                            ct += 1
                if ct >= k:
                    ct1 += 1
print(ct1)
