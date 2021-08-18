def main():
    n = int(input())
    p = list(map(int, input().split()))
    x = list(map(int, input().split()))
    g = [[] for _ in [0] * n]
    [g[j - 1].append(i + 1) for i, j in enumerate(p)]
    dist = [0] * n
    q = [0]
    while q:
        qq = q.pop()
        for i in g[qq]:
            if i != 0:
                dist[i] = dist[p[i - 1] - 1] + 1
                q.append(i)
    dist = sorted([[-j, i] for i, j in enumerate(dist)])
    dist = [j for i, j in dist]
    memo = [[i, 0] for i in x]
    for i in dist:
        if len(g[i]) == 0:
            continue
        dp = [10003] * (x[i] + 1)
        dp[0] = 0
        for j in g[i]:
            dp2 = [10003] * (x[i] + 1)
            for k in range(x[i] - memo[j][0], -1, -1):
                if dp[k] != 10003:
                    dp2[k + memo[j][0]] = min(dp2[k + memo[j][0]], dp[k] + memo[j][1], 5001)
            for k in range(x[i] - memo[j][1], -1, -1):
                if dp[k] != 10003:
                    dp2[k + memo[j][1]] = min(dp2[k + memo[j][1]], dp[k] + memo[j][0], 5001)
            dp = dp2
        memo[i][1] = min(dp)
        if memo[i][1] == 10003:
            print("IMPOSSIBLE")
            break
    else:
        print("POSSIBLE")


def __starting_point():
    main()


__starting_point()
