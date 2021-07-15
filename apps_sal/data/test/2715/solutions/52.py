import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    K = int(readline())

    N = 50

    q, r = divmod(K, N)
    A = [0] * N
    for i in range(N):
        if i < r:
            A[i] = N - 1 + (N + 1) * (q + 1) - K
        else:
            A[i] = N - 1 + (N + 1) * q - K

    print(N)
    print((*A))
    return


def __starting_point():
    main()

__starting_point()
