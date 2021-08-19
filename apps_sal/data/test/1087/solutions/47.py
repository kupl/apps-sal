import sys
input = sys.stdin.readline


def read():
    N, K = list(map(int, input().strip().split()))
    A = list(map(int, input().strip().split()))
    return N, K, A


def solve(N, K, A):
    L = max(K, max(A), 1).bit_length()
    k = [0 for i in range(L)]
    i = 0
    while K:
        k[i] += K & 1
        i += 1
        K >>= 1
    b = [0 for i in range(L)]
    for a in A:
        i = 0
        x = a
        while x:
            b[i] += x & 1
            i += 1
            x >>= 1
    k = k[::-1]
    b = b[::-1]
    # dp[i][1]: 上位iビットがKと等しいときの最大値
    # dp[i][0]: 上位iビットがKより小さいときの最大値
    dp = [[-1, -1] for i in range(L + 1)]
    dp[0][1] = 0
    for i in range(L):
        if dp[i][0] >= 0:
            dp[i + 1][0] = (dp[i][0] << 1) + max(b[i], N - b[i])
        if dp[i][1] >= 0:
            if k[i] == 1:
                dp[i + 1][0] = max(dp[i + 1][0], (dp[i][1] << 1) + b[i])
                dp[i + 1][1] = (dp[i][1] << 1) + (N - b[i])
            else:
                dp[i + 1][1] = (dp[i][1] << 1) + (b[i])
    return max(dp[L][1], dp[L][0])


def __starting_point():
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print(("%s" % str(outputs)))


__starting_point()
