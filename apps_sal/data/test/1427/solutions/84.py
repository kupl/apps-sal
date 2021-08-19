from itertools import groupby


def fast_prime_factorization_many(lst):
    # 素因数分解（ロー法、複数）
    from subprocess import Popen, PIPE
    res = Popen(["factor"] + list(map(str, lst)), stdout=PIPE).communicate()[0].split(b"\n")[:-1]
    return [list(map(int, r.split()[1:])) for r in res]


def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9 + 7
    max_factor = [0] * (1010101)
    lcm = 1
    Factors = fast_prime_factorization_many(A)
    for factors in Factors:
        for prime, group in groupby(factors):
            n = len(list(group))
            n_old = max_factor[prime]
            if n_old < n:
                for i in range(n - n_old):
                    lcm = lcm * prime % mod
                max_factor[prime] = n
    ans = 0
    for a in A:
        ans += pow(a, mod - 2, mod)
    ans = ans * lcm % mod
    print(ans)


main()
