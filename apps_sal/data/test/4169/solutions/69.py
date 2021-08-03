import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M, *AB = list(map(int, read().split()))
    X = [(a, b) for a, b in zip(*[iter(AB)] * 2)]

    X.sort()

    ans = 0
    n = 0
    for a, b in X:
        if n + b >= M:
            ans += (M - n) * a
            break
        else:
            ans += a * b
            n += b

    print(ans)
    return


def __starting_point():
    main()


__starting_point()
