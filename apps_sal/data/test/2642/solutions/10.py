from collections import defaultdict
import math


def main():
    n = int(input())
    mod = 1000000007
    zeroes = 0
    quadrant1 = defaultdict(int)
    quadrant2 = defaultdict(int)

    for _ in range(n):
        a, b = map(int, input().split())
        if a == b == 0:
            zeroes += 1
            continue

        g = math.gcd(a, b)
        a, b = a // g, b // g

        if b < 0:
            a, b = -a, -b

        if a <= 0:
            a, b = b, -a
            quadrant1[(a, b)] += 0
            quadrant2[(a, b)] += 1
        else:
            quadrant1[(a, b)] += 1
            quadrant2[(a, b)] += 0

    ans = 1
    for key, value in quadrant1.items():
        now = 1
        now += pow(2, value, mod) - 1
        now += pow(2, quadrant2[key], mod) - 1
        ans = (ans * now) % mod

    ans += (zeroes - 1)
    return ans % mod


def __starting_point():
    print(main())


__starting_point()
