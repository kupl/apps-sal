import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())

    ans = 0
    rate = 380000.0
    for _ in range(N):
        x, u = readline().split()
        if u == 'JPY':
            ans += int(x)
        else:
            ans += float(x) * rate

    print(ans)
    return


def __starting_point():
    main()


__starting_point()
