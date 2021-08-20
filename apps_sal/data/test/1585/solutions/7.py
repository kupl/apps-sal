mod = 1000000007
eps = 10 ** (-9)


def main():
    import sys
    input = sys.stdin.readline
    (x, y) = list(map(int, input().split()))
    ans = 0
    while x <= y:
        ans += 1
        x *= 2
    print(ans)


def __starting_point():
    main()


__starting_point()
