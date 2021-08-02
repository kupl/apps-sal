import sys
from itertools import groupby

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()
    N = len(S)
    M = 10 ** 5
    K = len(bin(M)) - 2

    A = [[0] * N for _ in range(K)]
    for i, c in enumerate(S):
        if c == 'R':
            A[0][i] = i + 1
        else:
            A[0][i] = i - 1

    for k in range(K - 1):
        for i in range(N):
            A[k + 1][i] = A[k][A[k][i]]

    B = list(range(N))
    for k in range(K):
        if M & (1 << k):
            for i in range(N):
                B[i] = A[k][B[i]]

    ans = [0] * N
    for b in B:
        ans[b] += 1

    print((*ans))
    return


def __starting_point():
    main()


__starting_point()
