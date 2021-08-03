import sys
import numpy as np
from collections import deque, defaultdict


def inp(v, w): return v[0] * w[0] + v[1] * w[1]
def isprop(a, b): return a[0] * b[1] == a[1] * b[0]
def cwsum(l): return [sum([x[0] for x in l]), sum([x[1] for x in l])]


def chmin(a, b): return (a, b)[b < a]
# cwsum = lambda l:np.sum(l,axis=0)


def main():
    N, Ma, Mb = list(map(int, input().split()))
    infty = 10**9
    ch = [list(map(int, input().split())) for _ in range(N)]
    p = [(-1) * Mb, Ma]
    # cand=[v[2] for v in ch if inp(p,v[:2])==0]
    # if cand:
    # m1=min(cand)
    # else:
    # m1=infty
    # ncand=[v for v in ch if inp(p,v[:2])!=0] #p方向への射影
    pch = [[inp(v[:2], p), v[2]] for v in ch]
    X = N * max([abs(w[0]) for w in pch])
    dp = [[infty] * (2 * X + 1) for _ in range(N)]
    for i in range(N):
        for j in range(2 * X + 1):
            if i == 0 and j == X + pch[0][0]:
                dp[i][j] = pch[0][1]
            elif i > 0 and j == X + pch[i][0]:
                dp[i][j] = chmin(dp[i - 1][j], pch[i][1])
            elif i > 0 and j >= pch[i][0] and j <= 2 * X + pch[i][0]:
                dp[i][j] = chmin(dp[i - 1][j], dp[i - 1][j - pch[i][0]] + pch[i][1])
            elif i > 0:
                dp[i][j] = dp[i - 1][j]
    #  print(ch)
    #  print(pch)
    #  print(dp)
    if dp[N - 1][X] == infty:
        print((-1))
    else:
        print((dp[N - 1][X]))


def __starting_point():
    main()


__starting_point()
