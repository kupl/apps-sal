

def main():
    from itertools import accumulate
    import sys
    input = sys.stdin.readline

    n, k = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    a = list(accumulate([0] + [i for i in range(n + 1)]))
    ans = 0

    for j in range(k, n + 2):
        max_value = a[-1] - a[n + 1 - j]
        min_value = a[j]
        ans += (max_value - min_value) + 1
        ans %= mod

    print((ans % mod))


def __starting_point():
    main()


__starting_point()
