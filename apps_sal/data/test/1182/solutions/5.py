r, c, n, k = list(map(int, input().split()))
p = []
for i in range(r):
    p.append([0] * c)
for i in range(n):
    x, y = list(map(int, input().split()))
    p[x - 1][y - 1] = 1
ans = 0
for i in range(r):
    for t in range(c):
        for e in range(r):
            for g in range(c):
                col = 0
                for h in range(i, e + 1):
                    for f in range(t, g + 1):
                        col += p[h][f]
                if col >= k:
                    ans += 1
print(ans)
