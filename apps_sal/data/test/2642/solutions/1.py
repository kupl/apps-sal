def main():
    from collections import defaultdict
    from math import gcd
    import sys
    input = sys.stdin.readline

    mod = 10 ** 9 + 7
    n = int(input())
    fishes = defaultdict(int)
    zero_zero = 0
    zero = 0
    inf = 0

    for _ in range(n):
        a, b = list(map(int, input().split()))
        if a == 0 and b == 0:
            zero_zero += 1

        elif a == 0:
            zero += 1

        elif b == 0:
            inf += 1

        else:
            div = gcd(a, b)
            a //= div
            b //= div
            if b < 0:
                a *= -1
                b *= -1
            key = (a, b)
            fishes[key] += 1

    def get_bad_pair(fish):
        a, b = fish
        if a < 0:
            a *= -1
            b *= -1
        return (-b, a)

    ans = 1
    counted_key = set()
    for fish_key, count in list(fishes.items()):
        if fish_key in counted_key:
            continue

        bad_pair = get_bad_pair(fish_key)
        if bad_pair in fishes:
            pair_count = fishes[bad_pair]
            pattern = pow(2, count, mod) + pow(2, pair_count, mod) - 1
            counted_key.add(bad_pair)

        else:
            pattern = pow(2, count, mod)

        ans = ans * pattern % mod

    ans *= pow(2, zero, mod) + pow(2, inf, mod) - 1
    if zero_zero:
        ans += zero_zero

    ans -= 1
    print((ans % mod))


def __starting_point():
    main()


__starting_point()
