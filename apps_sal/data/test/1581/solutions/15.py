MOD = 10 ** 9 + 7


def main(N, K):
    W = []
    i = 1
    while i <= N:
        v = N // i
        j = N // v
        # keys.append((v, j - i + 1))
        W.append(j - i + 1)
        i += j - i + 1

    l = len(W)
    dp = [0] * l

    total = 0
    for i, w in enumerate(W):
        total += w
        dp[l - i - 1] = total

    for i in range(2, K + 1):
        tmp = [0] * l
        total = 0
        for j, w in enumerate(W):
            v = dp[j] * w
            total += v
            total %= MOD
            tmp[l - j - 1] = total

        dp = tmp

    return dp[0]


def __starting_point():
    N, K = list(map(int, input().strip().split()))
    # import time
    # t = time.time()
    print((main(N, K)))
    # print(time.time() - t)


__starting_point()
