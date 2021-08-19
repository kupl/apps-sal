from itertools import groupby
from collections import Counter


def fast_prime_factorization_many(lst):
    from subprocess import Popen, PIPE
    res = Popen(['factor'] + list(map(str, lst)), stdout=PIPE).communicate()[0].split(b'\n')[:-1]
    return [Counter(list(map(int, r.split()[1:]))) for r in res]


def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(1)
        return
    mod = int(1000000000.0 + 7)
    Factors = fast_prime_factorization_many(A)
    lcm = 1
    max_factor = [0] * 1000010
    for f in Factors:
        for (k, v) in list(f.items()):
            v_prev = max_factor[k]
            if v_prev < v:
                for i in range(v - v_prev):
                    lcm = lcm * k % mod
                max_factor[k] = v
    ans = 0
    for a in A:
        wk = lcm * pow(a, mod - 2, mod)
        ans += wk
        ans %= mod
    print(ans)
    return


main()
