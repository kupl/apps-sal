import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    F = [list(map(int, readline().split())) for _ in range(N)]
    P = [list(map(int, readline().split())) for _ in range(N)]
    ans = -INF
    for bits in range(1, 1 << 10):
        res = 0
        for i in range(N):
            c = 0
            for j in range(10):
                if F[i][j] and bits & 1 << j:
                    c += 1
            res += P[i][c]
        if ans < res:
            ans = res
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
