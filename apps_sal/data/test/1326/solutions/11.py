def func(n):
    return n * (n + 1) // 2


def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        ans += i * func(N // i)
    print(ans)


def __starting_point():
    main()


__starting_point()
