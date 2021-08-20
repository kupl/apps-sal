import sys
MOD = 998244353


def solve(N: int, K: int, L: 'List[int]', R: 'List[int]'):
    n = N + 1
    a = [0] * n
    s = [0] * n
    a[1] = 1
    s[1] = 1
    for i in range(2, n):
        for k in range(K):
            l = max(i - R[k], 0)
            r = max(i - L[k], 0)
            a[i] += s[r] - s[l - 1]
            a[i] %= MOD
        s[i] = s[i - 1] + a[i]
        s[i] %= MOD
    return a[N] % MOD


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
    print(solve(N, K, L, R))


def __starting_point():
    main()


__starting_point()
