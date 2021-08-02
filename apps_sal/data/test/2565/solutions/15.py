t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    x, y, z = map(int, input().split())
    ans = 0
    t = min(c, y)
    c -= t
    y -= t
    ans += t * 2
    t = min(z, c)
    z -= t
    c -= t
    t = min(z, a)
    z -= t
    a -= t
    ans -= min(z, b) * 2
    print(ans)
