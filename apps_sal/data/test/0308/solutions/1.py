import sys
ii = lambda: sys.stdin.readline().strip()
idata = lambda: [int(x) for x in ii().split()]
sdata = lambda: list(ii())


def solve():
    n, x, y, c = idata()
    r = n ** 2
    l = -1
    while l + 1 < r:
        middle = (l + r) // 2
        ans = 1 + 2 * (middle + 1) * middle
        ans -= pow(middle - n + y, 2) if middle - n + y > 0 else 0
        ans -= pow(middle + 1 - y, 2) if middle + 1 - y > 0 else 0
        ans -= pow(middle - n + x, 2) if middle - n + x > 0 else 0
        ans -= pow(middle + 1 - x, 2) if middle + 1 - x > 0 else 0
        d = 1 + n - x + y
        if middle >= d:
            ans += (middle - d + 1) * (middle - d + 2) // 2
        d = 2 + 2 * n - y - x
        if middle >= d:
            ans += (middle - d + 1) * (middle - d + 2) // 2
        d = 1 + n - y + x
        if middle >= d:
            ans += (middle - d + 1) * (middle - d + 2) // 2
        d = x + y
        if middle >= d:
            ans += (middle - d + 1) * (middle - d + 2) // 2
        if ans >= c:
            r = middle
        else:
            l = middle
    print(r)
    return


for t in range(1):
    solve()
