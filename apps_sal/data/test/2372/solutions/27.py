from heapq import heappop as hpp, heappush as hp
from numba import njit, b1, i4, i8, f8
import numpy as np
import sys


def input():
    return sys.stdin.readline().rstrip()


sys.setrecursionlimit(max(1000, 10 ** 9))


def write(x):
    return sys.stdout.write(x + '\n')


@njit((b1[:, :], i8, i8, i8, i8))
def main(ss, ch, cw, dh, dw):
    inf = 1 << 30
    (h, w) = ss.shape
    start = ch * w + cw
    goal = dh * w + dw
    n = h * w
    seen = np.full(n, inf, np.int64)
    seen[start] = 0
    q = [(0, start)]
    while q:
        (pnum, pu) = hpp(q)
        (ux, uy) = divmod(pu, w)
        if pu == goal:
            break
        for xx in range(-2, 3):
            for yy in range(-2, 3):
                if xx == yy == 0:
                    continue
                if abs(xx) + abs(yy) <= 1:
                    vv = 0
                else:
                    vv = 1
                (x, y) = (ux + xx, uy + yy)
                u = x * w + y
                num = pnum + vv
                if x < 0 or y < 0 or x >= h or (y >= w) or ss[x][y]:
                    continue
                if seen[u] > num:
                    seen[u] = num
                    hp(q, (num, u))
    val = seen[goal]
    if val == inf:
        return -1
    else:
        return val


(h, w) = map(int, input().split())
(ch, cw) = map(int, input().split())
(dh, dw) = map(int, input().split())
ch -= 1
cw -= 1
dh -= 1
dw -= 1
(rows, cols) = (h, w)
OK = '.'
NG = '#'
ss = np.array([[c == '#' for c in input()] for _ in range(h)])
print(main(ss, ch, cw, dh, dw))
