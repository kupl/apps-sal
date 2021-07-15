from collections import defaultdict
import math
import sys
input = sys.stdin.readline


def select_num(a, b, mod=1000000007):
    sum = pow(2, a, mod) + pow(2, b, mod) - 1
    return sum % mod


def dict_count(d, a, b):
    this = a / b
    pair = b / a
    if not d.get(this, False):
        d[this] = {"num": 0, "pair": pair}
    d[this]["num"] += 1


def main():
    MOD = 1000000007
    n = int(input())

    d = defaultdict(lambda: [0] * 2)
    zero = 0
    for i in range(n):
        a, b = map(int, input().split())
        if a == 0 or b == 0:
            if a == b == 0:
                n -= 1
                zero += 1
            elif a == 0:
                d[0][True] += 1
            elif b == 0:
                d[0][False] += 1

        else:
            gcd = math.gcd(a, b)
            a //= gcd
            b //= gcd

            if b < 0:
                a, b = -a, -b

            rot = False
            if a < 0:
                b, a = -a, b
                rot = True
            d[(a, b)][rot] += 1

    ans = 1
    for k, v in d.items():
        ans *= select_num(v[0], v[1], MOD)
        ans %= MOD

    ans += zero - 1
    ans %= MOD
    print(ans)


def __starting_point():
    main()
__starting_point()
