def sell(p, x, a, y, b, m):
    from math import gcd
    i2 = m // a
    i1 = i2 // (b // gcd(a, b))
    return x * sum(p[:i2]) + y * (sum(p[:i1]) + sum(p[i2:m // b + i2 - i1]))


def main():
    for _ in range(int(input())):
        n = int(input())
        p = sorted((int(pi) // 100 for pi in input().split()), reverse=True)
        (x, a) = list(map(int, input().split()))
        (y, b) = list(map(int, input().split()))
        if x < y:
            (x, a, y, b) = (y, b, x, a)
        k = int(input())
        (l_, r) = (0, n + 1)
        while r - l_ > 1:
            m = (l_ + r) // 2
            if sell(p, x, a, y, b, m) >= k:
                r = m
            else:
                l_ = m
        print(-1 if r > n else r)


main()
