import math
(m, a, b) = list(map(int, input().split()))
vis = [-1] * (a + b + 5)
now = 0
maxd = 0
while True:
    vis[now] = maxd
    if now >= b:
        now -= b
    else:
        now += a
    if now == 0:
        break
    maxd = max(maxd, now)
ans = 0
for i in range(0, a + b):
    if vis[i] != -1:
        ans += max(0, m - vis[i] + 1)
rest = m - (a + b) + 1
if m >= a + b:
    g = math.gcd(a, b)
    tmp = rest // g * g
    fir = rest - tmp
    lst = rest
    cnt = tmp // g + 1
    ans += (fir + lst) * cnt // 2
print(int(ans))
