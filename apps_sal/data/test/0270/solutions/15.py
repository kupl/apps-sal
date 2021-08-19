def solve():
    import sys
    input = sys.stdin.readline
    (N, M) = list(map(int, input().split()))
    adjL = [[] for _ in range(N)]
    outdegs = [0] * N
    for _ in range(M):
        (s, t) = list(map(int, input().split()))
        (s, t) = (s - 1, t - 1)
        adjL[s].append(t)
        outdegs[s] += 1
    probs = [0] * N
    probs[0] = 1
    for v in range(N):
        for v2 in adjL[v]:
            probs[v2] += probs[v] / outdegs[v]
    dp = [0] * N
    for v in reversed(list(range(N - 1))):
        dp[v] = sum([dp[v2] for v2 in adjL[v]]) / outdegs[v] + 1
    ans = dp[0]
    for vRem in range(N):
        if outdegs[vRem] == 1:
            continue
        (sumDP, maxDP) = (0, -1)
        for v2 in adjL[vRem]:
            sumDP += dp[v2]
            if dp[v2] > maxDP:
                maxDP = dp[v2]
        dp2 = (sumDP - maxDP) / (outdegs[vRem] - 1) + 1
        decre = dp[vRem] - dp2
        ans2 = dp[0] - decre * probs[vRem]
        ans = min(ans, ans2)
    print(ans)


solve()
