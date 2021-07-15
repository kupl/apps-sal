import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M, *AB = list(map(int, read().split()))

    Q = [[] for _ in range(N - 1)]
    for i, (a, b) in enumerate(zip(*[iter(AB)] * 2)):
        Q[a - 1].append(b - 2)

    min_y = INF
    ans = 0
    for i, ys in enumerate(Q):
        if ys:
            min_y = min(min_y, min(ys))
        if i == min_y:
            ans += 1
            min_y = INF

    print(ans)
    return


def __starting_point():
    main()

__starting_point()
