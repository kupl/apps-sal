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
    A = [N - 1 + (N + 1) * q - K] * N

    for i in range(r):
        A[i] += N + 1

    print(N)
    print((' '.join(map(str, A))))
    return


def __starting_point():
    main()

__starting_point()
