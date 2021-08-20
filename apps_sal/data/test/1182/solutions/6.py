(r, c, n, k) = [int(x) for x in input().split()]
mus = [[0 for j in range(c)] for i in range(r)]
for t in range(n):
    (x, y) = [int(s) - 1 for s in input().split()]
    mus[x][y] = 1
ans = 0
for i1 in range(r):
    for i2 in range(i1, r):
        for j1 in range(c):
            for j2 in range(j1, c):
                S = 0
                for x in range(i1, i2 + 1):
                    for y in range(j1, j2 + 1):
                        S += mus[x][y]
                if S >= k:
                    ans += 1
print(ans)
