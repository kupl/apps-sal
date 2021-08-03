def main():
    n, k = list(map(int, input().split()))
    s = [0] * n
    for i in map(int, input().split()):
        s[i - 1] = 1
    e = [[] for _ in range(n)]
    for _ in range(n - 1):
        x, y = (int(s) - 1 for s in input().split())
        e[x].append(y)
        e[y].append(x)
    q, fa = [0], [-1] * n
    fa[0] = 0
    for i in range(n):
        x = q[i]
        for y in e[x]:
            if fa[y] == -1:
                fa[y] = x
                q.append(y)
    dp, k2 = [0] * n, k * 2
    for x in reversed(q):
        for y in e[x]:
            if fa[y] == x:
                i = s[y]
                s[x] += i
                dp[x] += dp[y] + (k2 - i if i > k else i)
    print(dp[0])


def __starting_point():
    main()


__starting_point()
