mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    ans = 0
    a, b, c = list(map(int, input().split()))
    if a % 2 != c % 2 and b % 2 != c % 2:
        ans += 1
        a += 1
        b += 1
    elif b % 2 != a % 2 and c % 2 != a % 2:
        ans += 1
        b += 1
        c += 1
    elif c % 2 != b % 2 and a % 2 != b % 2:
        ans += 1
        c += 1
        a += 1
    a, b, c = sorted([a, b, c])
    ans += (c - a) // 2
    ans += (c - b) // 2
    print(ans)


def __starting_point():
    main()


__starting_point()
