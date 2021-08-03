from itertools import permutations
from itertools import accumulate
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline


def solve():
    INF = 10**15

    N, M = list(map(int, input().split()))
    Ws = list(map(int, input().split()))
    LVs = [tuple(map(int, input().split())) for _ in range(M)]

    minV = min([V for L, V in LVs])

    if max(Ws) > minV:
        print((-1))
        return

    LVs.sort(key=lambda x: x[1])
    bdrLs, bdrVs = [0], [0]
    maxL = 0
    for L, V in LVs:
        if L > maxL:
            bdrLs.append(L)
            bdrVs.append(V)
            maxL = L

    ans = INF
    for Camels in permutations(Ws, N):
        accCamels = [0] + list(accumulate(Camels))
        Lss = [[INF] * (N) for _ in range(N)]
        for i in range(N):
            if Camels[i] > minV:
                Lss[i][i] = INF
            else:
                Lss[i][i] = 0
            for j in range(i + 1, N):
                wgt = accCamels[j + 1] - accCamels[i]
                iV = bisect_left(bdrVs, wgt) - 1
                Lss[i][j] = bdrLs[iV]

        costs = [0] * N
        for i in range(1, N):
            cost = 0
            for j in range(i + 1):
                c2 = costs[j] + Lss[j][i]
                if c2 > cost:
                    cost = c2
            costs[i] = cost

        if costs[-1] < ans:
            ans = costs[-1]

    if ans == INF:
        print((-1))
    else:
        print(ans)


solve()
