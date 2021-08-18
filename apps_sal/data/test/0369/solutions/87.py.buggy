n, m = map(int, input().split())
a = list(map(int, list(input())))
dp = [-1] * (n + 1)
te = [-1] * (n + 1)
te[n] = 0
g = [n]
c = 0
r = n
for i in reversed(range(n)):
    if a[i]:
        continue
    if i + m < r:
        r = i + m
        while a[r]:
            r -= 1
        if r == i:
            print(-1)
            return
    dp[i] = r
    te[i] = te[r] + 1
    if c < te[i]:
        c += 1
        g.append(i)
    g[te[i]] = i
g = g[::-1]
d = [y - x for x, y in zip(g, g[1:])]
print(*d)
