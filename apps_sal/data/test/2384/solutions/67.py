import sys
#import copy
#import numpy as np
#import itertools
#import collections
#from collections import deque
#from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
#from scipy.sparse import csr_matrix

sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
#read = sys.stdin.buffer.read

inf = float('inf')
#inf = pow(10, 10)


def main():
    # input
    N = int(readline())
    A = list(map(int, readline().split()))

    K = N // 2
    DP0 = [-inf] * N
    DP1 = [-inf] * N
    DP2 = [-inf] * N

    DP2[0] = A[0]
    DP2[1] = max(A[0], A[1])
    DP1[:2] = [0] * 2
    DP0[:4] = [0] * 4
    for i in range(2, N):
        if i % 2 == 0:
            DP2[i] = DP2[i - 2] + A[i]
            DP1[i] = max(DP2[i - 1], DP1[i - 2] + A[i])
            DP0[i] = max(DP1[i - 1], DP0[i - 2] + A[i])
        else:
            DP2[i] = max(DP2[i - 2] + A[i], DP2[i - 1])
            DP1[i] = max(DP1[i - 1], DP1[i - 2] + A[i])
            DP0[i] = max(DP0[i - 1], DP0[i - 2] + A[i])

    if N % 2 == 0:
        ans = DP2[N - 1]
    else:
        ans = DP1[N - 1]

    # print(DP0)
    # print(DP1)
    # print(DP2)
    print(ans)


def __starting_point():
    main()


__starting_point()
