import sys
MOD = 998244353


def solve(N: int, K: int, L: 'List[int]', R: 'List[int]'):
    cum = [0] * (N + 1)
    dp = [0] * (N + 1)
    cum[1] = 1
    dp[1] = 1
    cnt = 0
    for i in range(2, N + 1):
        for j in range(K):
            li = i - L[j]
            ri = i - R[j]
            if li < 0:
                continue
            ri = max(ri, 1)
            dp[i] += cum[li] - cum[ri - 1]
        cum[i] = (cum[i - 1] + dp[i]) % MOD
    return print(dp[N] % MOD)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    K = int(next(tokens))
    L = [int()] * K
    R = [int()] * K
    for i in range(K):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(N, K, L, R)


def __starting_point():
    main()


__starting_point()
