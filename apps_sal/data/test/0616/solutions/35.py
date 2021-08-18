def chmin(l, i, v):
    if l[i] > v:
        l[i] = v
        return True
    return False


def main():
    N, M = map(int, input().split())
    keys = []
    for i in range(M):
        a, b = map(int, input().split())
        C = map(int, input().split())
        mask = 0
        for c in C:
            mask |= 1 << (c - 1)
        keys.append((a, mask))

    patterns = 1 << N
    INF = float("inf")
    dp = [INF] * patterns
    dp[0] = 0

    for a, mask in keys:
        for i in range(patterns):
            chmin(dp, i | mask, dp[i] + a)

    ans = dp[patterns - 1]
    print(-1 if ans == INF else ans)


def __starting_point():
    main()


__starting_point()
