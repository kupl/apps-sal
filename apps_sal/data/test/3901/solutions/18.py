from math import gcd


def main():
    n = int(input())
    a = b = list(map(int, input().split()))
    if 1 in b:
        print(n - b.count(1))
        return
    while b:
        b = [gcd(*p) for p in zip(a, b[1:])]
        if 1 in b:
            print(n * 2 - len(b) - 1)
            return
    print(-1)


def __starting_point():
    main()


__starting_point()
