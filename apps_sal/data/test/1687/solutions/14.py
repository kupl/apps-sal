import functools


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = functools.reduce(gcd, a)
    if ans not in a:
        print(-1)
    else:
        print(ans)


def __starting_point():
    main()


__starting_point()
