# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
# 
# 
# @stop_watch
def solve(N, As):
    S = sum(As)
    Xs = [0] * N
    Xs[0] = S - (sum(As[1::2]) * 2)
    for i in range(1, N):
        Xs[i] = 2 * As[i - 1] - Xs[i - 1]
    print((' '.join([str(i) for i in Xs])))


def __starting_point():
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    As = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    solve(N, As)

__starting_point()
