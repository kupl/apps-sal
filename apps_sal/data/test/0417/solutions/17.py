import sys

readline = sys.stdin.readline


def ns(): return readline().rstrip()
def ni(): return int(readline().rstrip())
def nm(): return list(map(int, readline().split()))
def nl(): return list(map(int, readline().split()))


def solve():
    n, x, d = nm()
    ans = 0
    if d == 0:
        print((1 if x == 0 else n + 1))
        return
    if d < 0:
        d = -d
        x = -x
    g = dict()
    g[0] = [(0, 0)]
    for i in range(1, n + 1):
        c, y = divmod(x * i, d)
        f = (c + i * (i - 1) // 2, c + n * i - i * (i + 1) // 2)
        if y not in g:
            g[y] = list()
        g[y].append(f)
    for y in g:
        f = sorted(g[y])
        cx, cy = f[0]
        for nx, ny in f:
            if nx <= cy:
                cx = min(nx, cx)
                cy = max(ny, cy)
            else:
                ans += cy - cx + 1
                cx, cy = nx, ny
        ans += cy - cx + 1
    print(ans)
    return


solve()
