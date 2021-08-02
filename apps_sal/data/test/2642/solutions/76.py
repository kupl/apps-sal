from collections import defaultdict
import math


def main():
    n = int(input())
    mod = 1000000007
    zeroes = 0
    counter1 = defaultdict(int)
    counter2 = defaultdict(int)
    for _ in range(n):
        x, y = [int(x) for x in input().split()]

        if x == y == 0:
            zeroes += 1
            continue

        denominator = math.gcd(x, y)
        x, y = x // denominator, y // denominator

        if y < 0:
            # quadrant III, IV -> I, II
            x, y = -x, -y

        if x <= 0:
            # round 90° from quadrant II to I
            x, y = y, -x
            counter2[(x, y)] += 1
            counter1[(x, y)] += 0
        else:
            counter1[(x, y)] += 1
            counter2[(x, y)] += 0

    ans = 1
    for k, v in list(counter1.items()):
        now = 1
        now += pow(2, v, mod) - 1
        now += pow(2, counter2[k], mod) - 1
        ans = ans * now % mod
    ans += zeroes
    ans -= 1  # choose no fish
    return ans % mod


def __starting_point():
    print((main()))


__starting_point()
