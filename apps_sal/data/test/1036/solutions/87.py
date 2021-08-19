def main():
    import sys
    import time
    input = sys.stdin.readline
    (N, K) = [int(x) for x in input().strip().split()]
    S = list(input().strip())
    janken = {('R', 'R'): 'R', ('R', 'S'): 'R', ('R', 'P'): 'P', ('S', 'R'): 'R', ('S', 'S'): 'S', ('S', 'P'): 'S', ('P', 'R'): 'P', ('P', 'S'): 'S', ('P', 'P'): 'P'}
    memo = {}

    def dp(k, p):
        if (k, p) in memo:
            return memo[k, p]
        if k == 1:
            return janken[S[p % N], S[(p + 1) % N]]
        memo[k, p] = janken[dp(k - 1, p * 2 % N), dp(k - 1, (p + 1) * 2 % N)]
        return memo[k, p]
    print(dp(K, 0))


def __starting_point():
    main()


__starting_point()
