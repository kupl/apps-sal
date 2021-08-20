import functools


def divmod(f, g):
    assert g
    h = 0
    for i in reversed(list(range(f.bit_length() - g.bit_length() + 1))):
        if f & 1 << g.bit_length() + i - 1:
            f ^= g << i
            h ^= 1 << i
    return (h, f)


def gcd(f, g):
    while g:
        (q, r) = divmod(f, g)
        (f, g) = (g, r)
    return f


def solve(n, x, a):
    g = functools.reduce(gcd, a)
    cnt = 0
    h = 0
    for k in reversed(list(range(x.bit_length() - g.bit_length() + 1))):
        bit = 1 << g.bit_length() + k - 1
        if x & bit:
            cnt += 1 << k
        if x & bit != h & bit:
            h ^= g << k
    cnt += h <= x
    return cnt % 998244353


def main():
    (n, x) = input().split()
    n = int(n)
    x = int(x, 2)
    a = [int(input(), 2) for _ in range(n)]
    print(solve(n, x, a))


def __starting_point():
    main()


__starting_point()
