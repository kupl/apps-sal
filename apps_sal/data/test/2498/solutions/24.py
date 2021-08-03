def main():
    import math
    n, m = list(map(int, input().split()))
    a = sorted(list(map(int, input().split())))
    for i in range(n):
        a[i] //= 2
    g = 1
    for i in range(n):
        g = a[i] * g // math.gcd(g, a[i])
    for i in range(n):
        if g // a[i] % 2 == 0:
            print((0))
            return
    if g > m:
        print((0))
        return
    print((1 + (m - g) // (2 * g)))


def __starting_point():
    main()


__starting_point()
