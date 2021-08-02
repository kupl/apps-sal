import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def f(n, a):
    ans = 0
    while n > 0:
        ans += n % a
        n //= a
    return ans


def main():
    N = int(readline())

    ans = INF
    for i in range(N + 1):
        ans = min(ans, f(i, 6) + f(N - i, 9))

    print(ans)
    return


def __starting_point():
    main()


__starting_point()
