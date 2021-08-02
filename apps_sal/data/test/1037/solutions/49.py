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
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for x in range(1, n + 1):
        ai, i = aii[x - 1]
        dp[x][0] = dp[x - 1][0] + ai * (i - x + 1)
        dp[0][x] = dp[0][x - 1] + ai * (n - x - i)

    for s in range(1, n + 1):
        for x in range(1, s):
            y = s - x
            ai, i = aii[s - 1]
            dp[x][y] = max(dp[x - 1][y] + ai * (i - x + 1),
                           dp[x][y - 1] + ai * (n - y - i))

    res = 0
    for x in range(n + 1):
        if dp[x][n - x] > res:
            res = dp[x][n - x]
    return res


def __starting_point():
    n = i1num()
    a = inums()
    aii = sorted([(a[i], i)for i in range(n)], reverse=True)
    print((solve(n, aii)))


__starting_point()
