MOD = 1000000007


def isSubset(a, b):
    return (a & b) == a


def isIntersect(a, b):
    return (a & b) != 0


def cntOrder(s, t):
    p = len(s)
    m = len(t)
    inMask = [0 for i in range(m)]
    for x in range(p):
        for i in range(m):
            if t[i] % s[x] == 0:
                inMask[i] |= 1 << x
    cnt = [0 for mask in range(1 << p)]
    for mask in range(1 << p):
        for i in range(m):
            if isSubset(inMask[i], mask):
                cnt[mask] += 1
    dp = [[0 for mask in range(1 << p)] for k in range(m + 1)]
    for i in range(m):
        dp[1][inMask[i]] += 1
    for k in range(m):
        for mask in range(1 << p):
            for i in range(m):
                if not isSubset(inMask[i], mask) and isIntersect(inMask[i], mask):
                    dp[k + 1][mask | inMask[i]] = (dp[k + 1][mask | inMask[i]] + dp[k][mask]) % MOD
            dp[k + 1][mask] = (dp[k + 1][mask] + dp[k][mask] * (cnt[mask] - k)) % MOD
    return dp[m][(1 << p) - 1]


def dfs(u):
    nonlocal a, graph, degIn, visited, s, t

    visited[u] = True
    if degIn[u] == 0:
        s.append(a[u])
    else:
        t.append(a[u])

    for v in graph[u]:
        if not visited[v]:
            dfs(v)


def main():
    nonlocal a, graph, degIn, visited, s, t
    n = int(input())
    a = list(map(int, input().split()))
    c = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        c[i][0] = 1
        for j in range(1, i + 1):
            c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % MOD
    degIn = [0 for u in range(n)]
    graph = [[] for u in range(n)]
    for u in range(n):
        for v in range(n):
            if u != v and a[v] % a[u] == 0:
                graph[u].append(v)
                graph[v].append(u)
                degIn[v] += 1
    ans = 1
    curLen = 0
    visited = [False for u in range(n)]
    for u in range(n):
        if not visited[u]:
            s = []
            t = []
            dfs(u)
            if len(t) > 0:
                sz = len(t) - 1
                cnt = cntOrder(s, t)
                ans = (ans * cnt) % MOD
                ans = (ans * c[curLen + sz][sz]) % MOD
                curLen += sz
    print(ans)


def __starting_point():
    main()


__starting_point()
