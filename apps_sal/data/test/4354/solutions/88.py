import sys

n, m = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(n)]
b = [list(map(int, input().split())) for i in range(m)]
chkPoint = [0] * n

for i, axy in enumerate(a):
    ax, ay = axy
    dist = sys.maxsize
    for j, bxy in enumerate(b):
        bx, by = bxy
        if dist > abs(ax - bx) + abs(ay - by):
            chkPoint[i] = j + 1
            dist = abs(ax - bx) + abs(ay - by)
    print((chkPoint[i]))
