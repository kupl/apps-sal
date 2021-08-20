import sys
MOD = 1000000007


def solve(N: int, K: int):
    num_gcd = {}
    for k in range(K, 0, -1):
        num_select = K // k
        num_gcd_k = pow(num_select, N, MOD)
        for multiple in range(2, num_select + 1):
            num_gcd_k -= num_gcd[k * multiple]
        num_gcd[k] = num_gcd_k
    result = 0
    for k in range(1, K + 1):
        result += k * num_gcd[k] % MOD
    print(result % MOD)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    K = int(next(tokens))
    solve(N, K)


def __starting_point():
    main()


__starting_point()
