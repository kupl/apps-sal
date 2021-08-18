import heapq as hq
import itertools
import math
import collections
def ma(): return map(int, input().split())
def lma(): return list(map(int, input().split()))
def tma(): return tuple(map(int, input().split()))
def ni(): return int(input())
def yn(fl): return print("Yes") if fl else print("No")


ceil = math.ceil
a, b = ma()
wh = "."
bl = "
if a > b:
    a, b = b, a
    wh, bl = bl, wh
area = [[wh] * 100 for i in range(100)]


def cycle(y, x, f=True):
    for i in range(y, y + 3):
        for j in range(x, x + 3):
            area[i][j] = bl
    if f:
        area[y + 1][x + 1] = wh


def solve():
    cnt = 0
    iy = 0
    ix = 0
    while cnt < b:
        if cnt + 1 < a:
            cycle(iy, ix)
        else:
            cycle(iy, ix, f=False)
        ix += 4
        if ix >= 95:
            ix = 0
            iy += 4
        cnt += 1


solve()
print(100, 100)
for ar in area:
    print("".join(ar))
