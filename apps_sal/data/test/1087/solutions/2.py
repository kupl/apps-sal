import sys
readline = sys.stdin.readline
MAX_DIGIT = 40


def main():
    N, K = map(int, readline().rstrip().split())
    K_bin = bin(K)[2:].zfill(MAX_DIGIT)
    A = list(map(int, readline().rstrip().split()))
    A = [bin(a)[2:].zfill(MAX_DIGIT) for a in A]
    dp = [[-1] * 2 for _ in range(MAX_DIGIT + 1)]

    dp[0][0] = 0
    mul = 2 ** (MAX_DIGIT - 1)
    for d in range(MAX_DIGIT):
        cnt = len([1 for a in A if a[d] == '1'])
        gain0 = cnt * mul
        gain1 = (N - cnt) * mul

        if dp[d][1] != -1:
            dp[d + 1][1] = max(dp[d + 1][1], dp[d][1] + max(gain0, gain1))

        if dp[d][0] != -1:
            if K_bin[d] == '1':
                dp[d + 1][1] = max(dp[d + 1][1], dp[d][0] + gain0)

        if dp[d][0] != -1:
            if K_bin[d] == '1':
                dp[d + 1][0] = max(dp[d + 1][0], dp[d][0] + gain1)
            else:
                dp[d + 1][0] = max(dp[d + 1][0], dp[d][0] + gain0)

        mul //= 2

    print(max(dp[MAX_DIGIT]))


def __starting_point():
    main()


__starting_point()
