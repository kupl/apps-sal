from math import gcd
from functools import reduce
import sys
input = sys.stdin.readline


def lcm(a, b):
    return a * b // gcd(a, b)


def count_factor_2(num):
    count = 0
    while num % 2 == 0:
        num //= 2
        count += 1
    return count


def main():
    (n, m) = list(map(int, input().split()))
    A = list([int(x) // 2 for x in input().split()])
    check = len(set(map(count_factor_2, A)))
    if check != 1:
        print(0)
        return
    lcm_a = reduce(lcm, A)
    step = lcm_a * 2
    ans = (m + lcm_a) // step
    print(ans)


def __starting_point():
    main()


__starting_point()
