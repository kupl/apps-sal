import heapq
import numpy as np
from numba import njit, i8, b1

h, w = map(int, input().split())
sh, sw = map(int, input().split())
gh, gw = map(int, input().split())
s = np.array([list(input()) for _ in range(h)]) == "#"


@njit(i8(i8, i8, i8, i8, i8, i8, b1[:, :]))
def solve(h, w, sh, sw, gh, gw, s):

    sh -= 1
    sw -= 1
    gh -= 1
    gw -= 1

    INF = 10**7
    dist = [[INF] * w for _ in range(h)]
    dist[sh][sw] = 0
    q = [(0, sh, sw)]
    while q:

        d, vsh, vsw = heapq.heappop(q)

        for dh in range(-2, 3):
            for dw in range(-2, 3):
                newh = vsh + dh
                neww = vsw + dw
                if newh < 0 or h <= newh or neww < 0 or w <= neww:
                    continue
                if dh == 0 and dw == 0:
                    continue
                if s[newh][neww]:
                    continue

                if abs(dh) + abs(dw) == 1:
                    if dist[newh][neww] > d:
                        dist[newh][neww] = d
                        if newh == gh and neww == gw:
                            return d
                        heapq.heappush(q, (d, newh, neww))
                else:
                    if dist[newh][neww] > d + 1:
                        dist[newh][neww] = d + 1
                        heapq.heappush(q, (d + 1, newh, neww))
    if dist[gh][gw] == INF:
        return -1
    else:
        return dist[gh][gw]


print(solve(h, w, sh, sw, gh, gw, s))
