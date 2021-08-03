import sys


def comb(n, r, mod=None):
    if r == 0 or r == n:
        return 1
    r = min([r, n - r])
    x, y = 1, 1
    ans = 1
    for i in range(1, r + 1):
        if mod:
            x *= n + 1 - i
            y *= i
            x %= mod
            y %= mod
        else:
            ans *= n + 1 - i
            ans //= i
    ans = x * pow(y, mod - 2, mod) % mod if mod else ans
    return ans


def main():
    input = sys.stdin.readline
    h, w, a, b = map(int, input().split())
    mod = pow(10, 9) + 7

    bef, aft = 1, comb(h + w - b - 2, h - 1, mod)
    ans = 0
    for i in range(h - a):
        ans += bef * aft
        ans %= mod

        bef = bef * (i + b) * pow(i + 1, mod - 2, mod) % mod
        aft = aft * (h - i - 1) * pow(h - i + w - b - 2, mod - 2, mod) % mod

    print(ans)


def __starting_point():
    main()


__starting_point()
