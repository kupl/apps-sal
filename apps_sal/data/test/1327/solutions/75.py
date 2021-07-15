import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M, *XYZ = list(map(int, read().split()))

    def score(s_X, s_Y, s_Z):
        P = [0] * N
        for i, (x, y, z) in enumerate(zip(*[iter(XYZ)] * 3)):
            P[i] = s_X * x + s_Y * y + s_Z * z

        P.sort(reverse=True)
        return sum(P[:M])

    ans = -INF
    for s_X in (-1, 1):
        for s_Y in (-1, 1):
            for s_Z in (-1, 1):
                res = score(s_X, s_Y, s_Z)
                if ans < res:
                    ans = res

    print(ans)

    return


def __starting_point():
    main()

__starting_point()
