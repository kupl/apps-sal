import sys
from heapq import heappush, heappop
def input(): return sys.stdin.readline().rstrip()
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())


def main():
    n = ii()
    x = [0] * n
    y = [0] * n
    h = [0] * n
    for i in range(n):
        x[i], y[i], h[i] = mi()
    idx = h.index(max(h))
    for cx in range(101):
        for cy in range(101):
            flag = True
            H = abs(cx - x[idx]) + abs(cy - y[idx]) + h[idx]
            for i in range(n):
                tmp = abs(cx - x[i]) + abs(cy - y[i])
                if h[i] == 0:
                    flag &= (tmp >= H)
                else:
                    tmp += h[i]
                    flag &= (tmp == H)
            if flag:
                print(cx, cy, H)
                return


def __starting_point():
    main()


__starting_point()
