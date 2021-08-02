n, k = map(int, input().split())
v = list(map(int, input().split()))
ans = 0
for i in range(min(n + 1, k + 1)):
    for j in range(min(n + 1 - i, k + 1 - i)):
        g = []
        x = 0
        while x < i:
            g.append(v[x])
            x += 1
        y = 0
        z = -1
        while y < j:
            g.append(v[z])
            y += 1
            z -= 1
        g.sort()
        x = k - i - j
        for z in range(min(len(g), x)):
            if g[z] < 0:
                g[z] = 0
            else:
                break
        ans = max(ans, sum(g))
print(ans)
