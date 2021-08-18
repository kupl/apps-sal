from collections import deque
from heapq import heappop, heappush

import numpy as np

from numba import njit


@njit('UniTuple(i8[:],4)(i1[:],i8,i8,i8)')
def reachable(field, h2, w2, k):
    hw = h2 * w2
    up = np.full(hw, -1, dtype=np.int64)
    dw = np.full(hw, -1, dtype=np.int64)
    lf = np.full(hw, -1, dtype=np.int64)
    rg = np.full(hw, -1, dtype=np.int64)
    lf_tmp = -1
    for i in range(w2, hw - w2):
        if field[i]:
            if lf_tmp == -1:
                lf_tmp = i
            lf[i] = max(lf_tmp, i - k)
        else:
            lf_tmp = -1
    rg_tmp = -1
    for i in range(hw - w2, w2 - 1, -1):
        if field[i]:
            if rg_tmp == -1:
                rg_tmp = i
            rg[i] = min(rg_tmp, i + k)
        else:
            rg_tmp = -1
    wk = w2 * k
    for j in range(1, w2):
        up_tmp = -1
        for i in range(j, hw, w2):
            if field[i]:
                if up_tmp == -1:
                    up_tmp = i
                up[i] = max(up_tmp, i - wk)
            else:
                up_tmp = -1
        dw_tmp = 0
        for i in range(hw - w2 + j, w2 - 1, -w2):
            if field[i]:
                if dw_tmp == -1:
                    dw_tmp = i
                dw[i] = min(dw_tmp, i + wk)
            else:
                dw_tmp = -1
    return up, dw, lf, rg


@njit('i8(i8,i8,i8,i1[:],i8,i8,i8,i8)')
def solve(h2, w2, k, field, x1, y1, x2, y2):
    s = x1 * w2 + y1
    t = x2 * w2 + y2
    up, dw, lf, rg = reachable(field, h2, w2, k)

    INF = 10 ** 18
    ans = [[INF, INF] for _ in field]
    ans[s][0] = ans[s][1] = 0

    q = [(0, s)]
    while q:
        cost, v = heappop(q)
        if v == t:
            return cost
        nc = cost + 1

        for u in range(up[v], v, w2):
            if ans[u][0] <= nc:
                break
            ans[u][0] = nc
            heappush(q, (nc, u))

        for u in range(dw[v], v, -w2):
            if ans[u][0] <= nc:
                break
            ans[u][0] = nc
            heappush(q, (nc, u))

        for u in range(lf[v], v, 1):
            if ans[u][1] <= nc:
                break
            ans[u][1] = nc
            heappush(q, (nc, u))

        for u in range(rg[v], v, -1):
            if ans[u][1] <= nc:
                break
            ans[u][1] = nc
            heappush(q, (nc, u))

    return -1


h, w, k = list(map(int, input().split()))
x1, y1, x2, y2 = list(map(int, input().split()))
h2 = h + 2
w2 = w + 2

field_tmp = [input() for _ in range(h)]
field = [0] * w2
for row in field_tmp:
    field.append(0)
    field.extend(list(map('@.'.index, row)))
    field.append(0)
field.extend([0] * w2)
field = np.array(field, dtype=np.int8)
print((solve(h2, w2, k, field, x1, y1, x2, y2)))
