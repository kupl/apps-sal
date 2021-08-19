import math
import sys
from itertools import accumulate
sys.setrecursionlimit(10 ** 8)
INF = float('inf')


def array(*args, initial=0):
    pre = '[' * len(args)
    post = ''
    for a in args[::-1]:
        post += ' for _ in range(' + str(a) + ')]'
    S = pre + str(initial) + post
    return eval(S)


def solve(N: int, A: 'List[int]'):
    if N % 2 == 0:
        K = 2
    else:
        K = 3
    DP = array(N, K, initial=-10 ** 9)
    DP[0][0] = A[0]
    DP[1][1] = A[1]
    if K == 3:
        DP[2][2] = A[2]
    for i in range(1, N):
        for k in range(K):
            if i == k and i < K:
                continue
            DP[i][k] = DP[i - 2][k]
            if k - 1 >= 0:
                DP[i][k] = max(DP[i][k], DP[i - 3][k - 1])
            if k - 2 >= 0:
                DP[i][k] = max(DP[i][k], DP[i - 4][k - 2])
            DP[i][k] += A[i]
    if N % 2 == 0:
        print(max(DP[-1][1], DP[-2][0]))
    else:
        print(max(DP[-1][2], DP[-2][1], DP[-3][0]))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    A = [int(next(tokens)) for _ in range(N)]
    solve(N, A)


def __starting_point():
    main()


__starting_point()
