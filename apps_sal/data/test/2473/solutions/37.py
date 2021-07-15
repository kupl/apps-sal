def abc075_d():
    n, k = map(int, input().split())
    P = []
    xarr = []
    yarr = []
    for _ in range(n):
        x, y = (int(x) for x in input().split())
        P.append((x, y))
        xarr.append(x)
        yarr.append(y)
    xarr.sort()
    yarr.sort()

    ans = 5*10**18
    for s, xi in enumerate(xarr):
        for xj in xarr[s+1:]:
            cand = [(x, y) for x, y in P if xi <= x and x <= xj]
            for t, yi in enumerate(yarr):
                for yj in yarr[t+1:]:
                    cnt = len([y for x, y in cand if yi <= y and y <= yj])
                    if cnt >= k:
                        area = (xj - xi) * (yj - yi)
                        ans = min(ans, area)
    print(ans)

def __starting_point():
    abc075_d()
__starting_point()
