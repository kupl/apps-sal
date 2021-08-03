def main():
    from math import gcd
    a, b = list(map(int, input().split()))
    g, res = gcd(a, b), 0
    for x in a // g, b // g:
        for p in 2, 3, 5:
            while not x % p:
                x //= p
                res += 1
        if x != 1:
            print(-1)
            return
    print(res)


def __starting_point():
    main()


__starting_point()
