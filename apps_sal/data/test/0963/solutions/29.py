def main():
    import sys
    input = sys.stdin.readline

    mod = 998244353

    n, k = list(map(int, input().split()))
    bk = []
    for _ in range(k):
        dl, dr = list(map(int, input().split()))
        bk.append((dl, dr))

    dp = [0] * (n + 1)
    dp[1] = 1

    acc = [0] * (n + 1)
    acc[1] = 1

    for i in range(2, n + 1):
        for dl, dr in bk:
            r = i - dl
            if r < 1:
                continue
            l = max(1, i - dr)
            dp[i] = (dp[i] + acc[r] - acc[l - 1]) % mod
        acc[i] = (acc[i - 1] + dp[i]) % mod
    print((dp[-1]))


def __starting_point():
    main()

__starting_point()
