import math

def test(k):
    nonlocal sm, mn, h
    return h + k * sm + mn <= 0


h, n = map(int, input().split())
a = list(map(int, input().split()))
mn = math.inf
sm = 0
for e in a:
    sm += e
    mn = min(mn, sm)
if mn >= 0:
    print(-1)
    return
l = -1
r = h + 1
while r - l > 1:
    m = (r + l) // 2
    if test(m):
        r = m
    else:
        l = m
h += sm * r
if h <= 0:
    print(n * r)
    return
for i in range(n):
    h += a[i]
    if h <= 0:
        print(r * n + i + 1)
        return
print(-1)
