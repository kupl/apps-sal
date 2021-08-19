import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15


def main():
    (N, M) = map(int, input().split())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    height = sum(((Y[i + 1] - Y[i]) * (i + 1) * (M - i - 1) % MOD for i in range(M - 1))) % MOD
    ans = sum((height * (X[i + 1] - X[i]) * (i + 1) * (N - i - 1) % MOD for i in range(N - 1))) % MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
