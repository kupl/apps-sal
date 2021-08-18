import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
z = list(range(n))
d = []
for i, j, k in zip(a, c, z):
    d.append([j, i, k])
d.sort(key=lambda x: -x[0])
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    ans = 0
    if a[x]:
        if a[x] >= y:
            print(c[x] * y)
            a[x] -= y
            continue
        else:
            ans += a[x] * c[x]
            y -= a[x]
            a[x] = 0
    while d and y > 0:
        q, w, e = d.pop()
        w = a[e]
        if w >= y:
            ans += q * y
            a[e] = w - y
            y = 0
            d.append([q, w - y, e])
        else:
            ans += w * q
            a[e] = 0
            y -= w
    if y:
        print(0)
    else:
        print(ans)
