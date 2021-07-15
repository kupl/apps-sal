def solve():
    u, v, w = map(int, input().split())
    x, y, z = map(int, input().split())
    ans = min(w, y) * 2
    w, y = w - min(w, y), y - min(w, y)
    z, u = z - min(z, u), u - min(z, u)
    z, w = z - min(z, w), w - min(z, w)
    v, x = v - min(v, x), u - min(v, x)
    v, y = v - min(v, y), v - min(v, y)
    ans -= min(v, z) * 2
    print(ans)
t = int(input())
for _ in range(t):
    solve()
