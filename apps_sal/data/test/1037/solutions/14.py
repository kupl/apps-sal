def i1str():
    return input()


def istrs(n=None):
    if n is None:
        return input().split()
    a = []
    for _ in range(n):
        a.append(istrs())
    return a


def i1num():
    return int(input())


def inums(n=None):
    if n is None:
        return list(map(int, input().split()))
    a = []
    for _ in range(n):
        a.append(inums())
    return a


def ostrs(l, sp=" "):
    print((sp.join(l)))


def onums(l, sp=" "):
    print((sp.join(map(str, l))))


def solve(n, aii):
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for x in range(n+1):
        for y in range(n+1-x):
            if x == y == 0:
                continue
            ai, i = aii[n-x-y]
            dp[x][y] = max(dp[x-1][y] + ai * (i-x+1) if x > 0 else 0,
                           dp[x][y-1] + ai * (n-y-i) if y > 0 else 0)

    res = 0
    for x in range(n+1):
        if dp[x][n-x] > res:
            res = dp[x][n-x]
    return res


def __starting_point():
    n = i1num()
    a = inums()
    aii = sorted((a[i], i)for i in range(n))
    print((solve(n, aii)))

__starting_point()
