from collections import deque
n, d, a = map(int, input().split())
xh = [list(map(int, input().split())) for _ in range(n)]
xh.sort(key=lambda x: x[0])
minusd = deque()
nowd = 0
ans = 0
for x, h in xh:
    while minusd and minusd[0][1] <= x:
        d_, _ = minusd.popleft()
        nowd -= d_
    tmp = max(0, (h - nowd + a - 1) // a)
    ans += tmp
    nowd += tmp * a
    minusd.append([tmp * a, x + 2 * d + 1])
print(ans)
