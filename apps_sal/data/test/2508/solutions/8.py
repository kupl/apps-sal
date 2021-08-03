from heapq import heapify, heappush as hpush, heappop as hpop
import sys
def input(): return sys.stdin.readline().rstrip()


H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
X = [1] * (W + 2)
for _ in range(H):
    X += [1] + [1 if a == "@" else 0 for a in input()] + [1]
X += [1] * (W + 2)
X += X[:]
H, W = H + 2, W + 2
HW = H * W
s, t = x1 * W + y1, x2 * W + y2
ss, tt = s + HW, t + HW


def dijkstra():
    n = 2 * H * W
    h = [(0, s), (0, ss)]
    D = [-1] * n
    done = [0] * n
    D[s] = 0
    D[ss] = 0
    while h:
        d, i = hpop(h)
        done[i] = 1
        if i < HW:
            for j in (i + 1, i - 1):
                nd = d + 1
                if X[j]:
                    continue
                if D[j] < 0 or D[j] > nd:
                    if done[j] == 0:
                        hpush(h, (nd, j))
                        D[j] = nd
        else:
            for j in (i + W, i - W):
                nd = d + 1
                if X[j]:
                    continue
                if D[j] < 0 or D[j] > nd:
                    if done[j] == 0:
                        hpush(h, (nd, j))
                        D[j] = nd

        j = i + HW if i < HW else i - HW
        nd = (d + K - 1) // K * K
        if X[j]:
            continue
        if D[j] < 0 or D[j] > nd:
            if done[j] == 0:
                hpush(h, (nd, j))
                D[j] = nd
    return [-(-a // K) for a in (D[t], D[tt]) if a >= 0]


di = dijkstra()
print(min(di) if di else -1)
