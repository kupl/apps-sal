#!/usr/bin/env python3

import itertools

def solve(L, n, px, py, x, y):
    for i in range(n):
        j = i + L
        if j > n:
            break
        dx = px[i] + px[-1] - px[j] - x
        dy = py[i] + py[-1] - py[j] - y
        if abs(dx) + abs(dy) <= L:
            return True
    return False

def main(args):
    n = int(input())
    d = input()
    x, y = list(map(int, input().split()))
    py = [0] + [1 if c == 'U' else (-1 if c == 'D' else 0) for c in d]
    px = [0] + [1 if c == 'R' else (-1 if c == 'L' else 0) for c in d]
    if abs(x+ y)%2 != n%2:
        print(-1)
        return 0
    py = list(itertools.accumulate(py))
    px = list(itertools.accumulate(px)) 
    if px[-1] == x and py[-1] == y:
        print(0)
        return 0
    if abs(x) + abs(y) > n:
        print(-1)
        return 0
    left = 0
    right = n
    while left + 1 < right:
        mid = (left + right) // 2
        if solve(mid, n, px, py, x, y):
            left, right = left, mid
        else:
            left, right = mid, right
    print(right)
    return 0

def __starting_point():
    import sys
    return(main(sys.argv))

__starting_point()
