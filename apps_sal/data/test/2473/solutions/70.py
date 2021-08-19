(n, k) = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
ax = sorted(a)
ans = 10 ** 19
for i in range(n - 1):
    for j in range(i + 1, n):
        a_use = ax[i:j + 1]
        xnum = len(a_use)
        sx = a_use[-1][0] - a_use[0][0]
        a_use.sort(key=lambda x: x[1])
        if xnum < k:
            continue
        for y1 in range(xnum - k + 1):
            y2 = y1 + k - 1
            s = sx * (a_use[y2][1] - a_use[y1][1])
            ans = min(ans, s)
print(ans)
