def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    ans = 0
    for a in range(1, n):
        ans += (n - 1) // a
    print(ans)


def __starting_point():
    main()


__starting_point()
