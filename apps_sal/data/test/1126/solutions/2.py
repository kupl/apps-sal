from collections import defaultdict
import sys
input = sys.stdin.readline


def read():
    (N, X, M) = list(map(int, input().strip().split()))
    return (N, X, M)


def solve(N, X, M):
    D = 34
    A = [[0 for j in range(M)] for i in range(D)]
    S = [[0 for j in range(M)] for i in range(D)]
    for j in range(M):
        A[0][j] = j * j % M
        S[0][j] = j
    for i in range(0, D - 1):
        for j in range(M):
            A[i + 1][j] = A[i][A[i][j]]
            S[i + 1][j] = S[i][j] + S[i][A[i][j]]
    ans = 0
    x = X
    for i in range(D - 1, -1, -1):
        if N & 1 << i == 1 << i:
            ans += S[i][x]
            x = A[i][x]
    return ans


def __starting_point():
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print('%s' % str(outputs))


__starting_point()
