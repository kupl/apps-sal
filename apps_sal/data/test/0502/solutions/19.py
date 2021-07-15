from math import *

ax, ay, bx, by, cx, cy = list(map(int, input().split()))

l1 = (bx - ax)**2 + (by - ay)**2
l2 = (cx - bx)**2 + (cy - by)**2
dx = bx - ax
dy = by - ay

if l1 != l2:
    print('No')
elif cx == bx + dx and cy == by + dy:
    print('No')
else:
    print('Yes')

