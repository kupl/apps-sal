from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)
def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]


def main():
    n, k = MI()
    xx = set()
    yy = set()
    xy = []
    for _ in range(n):
        x, y = MI()
        xy.append((x, y))
        xx.add(x)
        yy.add(y)
    xy.sort()
    xx = list(sorted(xx))
    yy = list(sorted(yy))
    xn = len(xx)
    yn = len(yy)
    ans = 10**20
    for t in range(yn):
        y2 = yy[t]
        for b in range(t):
            y1 = yy[b]
            r = -1
            s = 0
            i = j = 0
            for l, x1 in enumerate(xx):
                while i < n and xy[i][0] < x1:
                    if y1 <= xy[i][1] <= y2:
                        s -= 1
                    i += 1
                while s < k and r + 1 < xn:
                    r += 1
                    x2 = xx[r]
                    while j < n and xy[j][0] <= x2:
                        if y1 <= xy[j][1] <= y2:
                            s += 1
                        j += 1
                if s >= k:
                    cur = (x2 - x1) * (y2 - y1)
                    if cur < ans:
                        ans = cur
    print(ans)


main()
