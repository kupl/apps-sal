# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, S):
    sachi = 0
    L_cluster, R_cluster = (0, 1) if S[0] == 'R' else (1, 0)
    for i in range(N):
        if S[i] == 'R' and i != N - 1 and S[i + 1] == 'R':
            sachi += 1
        if S[i] == 'L' and i != 0 and S[i - 1] == 'L':
            sachi += 1
        if i > 0 and S[i] != S[i - 1]:
            if S[i] == 'R':
                R_cluster += 1
            else:
                L_cluster += 1

    ans = 0
    reverse_cluster = min(L_cluster, R_cluster)
    if K >= reverse_cluster:
        ans = N - 1
    else:
        ans = sachi + K * 2

    print(ans)


def __starting_point():
    # N = int(input())
    N, K = list(map(int, input().split()))
    S = input()
    # As = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    solve(N, K, S)


__starting_point()
