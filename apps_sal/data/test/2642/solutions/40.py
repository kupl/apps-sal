def main():
    import sys
    sys.setrecursionlimit(10**9)
    input = sys.stdin.readline
    import math
    from collections import defaultdict

    mod = 1000000007

    N = int(input())

    zero_pair = 0
    zero_a = 0
    zero_b = 0
    pair_plus = defaultdict(int)
    pair_minus = defaultdict(int)
    for a, b in [tuple(map(int, input().split())) for _ in range(N)]:
        if a == 0 and b == 0:
            zero_pair += 1
            continue
        if a == 0:
            zero_a += 1
            continue
        if b == 0:
            zero_b += 1
            continue

        abs_a = abs(a)
        abs_b = abs(b)
        g = math.gcd(abs_a, abs_b)
        abs_a = abs_a // g
        abs_b = abs_b // g
        if a * b > 0:
            pair_plus[(abs_a, abs_b)] += 1
        else:
            pair_minus[(abs_a, abs_b)] += 1

    ans = 1
    ans *= (pow(2, zero_a, mod) + pow(2, zero_b, mod) - 1) % mod
    ans %= mod

    count_all = 0
    for item in list(pair_plus.items()):
        a, b = item[0]
        cnt = item[1]
        if (b, a) in pair_minus:
            ans *= (pow(2, cnt, mod) + pow(2, pair_minus[(b, a)]) - 1) % mod
            ans %= mod
            del pair_minus[(b, a)]
        else:
            count_all += cnt

    for val in list(pair_minus.values()):
        count_all += val

    ans = (ans * pow(2, count_all, mod)) % mod
    ans += zero_pair
    print(((ans - 1) % mod))


main()
