#!/usr/bin/env python3
import sys
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return [LIST() for _ in range(n)]

def main():
    from heapq import heappush, heappop, heapify
    H, W, K = MAP()
    HH = max(H, W) + 2
    x1, y1, x2, y2 = LIST()
    c = [[-1] + [0 if c == "." else -1 for c in input()] + [-1]
         for i in range(H)]
    c = [[-1] * (W + 2)] + c + [[-1] * (W + 2)]

    # 0123: 上下左右
    stack = []
    heappush(stack, (0, x1, y1, 0))
    heappush(stack, (0, x1, y1, 1))
    heappush(stack, (0, x1, y1, 2))
    heappush(stack, (0, x1, y1, 3))
    DX = (1, 0, -1, 0)
    DY = (0, 1, 0, -1)
    while stack:
        new_stack = []
        while stack:
            curr, x, y, d = heappop(stack)
            dx, dy = DX[d], DY[d]
            flag = True
            a = curr + 1
            for k in range(1, K + 1):
                xx, yy = x + k * dx, y + k * dy
                if c[xx][yy] == 0:
                    b = c[xx + DX[(d - 1) % 4]][yy + DY[(d - 1) % 4]]
                    if b == 0 or b == a + 1:
                        heappush(new_stack, (a, xx, yy, (d - 1) % 4))
                    b = c[xx + DX[(d + 1) % 4]][yy + DY[(d + 1) % 4]]
                    if b == 0 or b == a + 1:
                        heappush(new_stack, (a, xx, yy, (d + 1) % 4))
                    c[xx][yy] = a
                elif c[xx][yy] != a:
                    flag = False
                    break
            if flag:
                heappush(new_stack, (a, xx, yy, d))
            if c[x2][y2] > 0:
                print(c[x2][y2], flush=True)
                return
        stack = new_stack

    print(-1)
    return


def __starting_point():
    main()

__starting_point()
