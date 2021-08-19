import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        ans += i * (1 + n // i) * (n // i) // 2
    print(ans)


def __starting_point():
    main()


__starting_point()
