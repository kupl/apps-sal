import sys
nx = list(map(int, sys.stdin.readline().split()))
n = nx[0]
x = nx[1]
lr = [[0, 0]]
for i in range(0, n):
    g = list(map(int, sys.stdin.readline().split()))
    lr = lr + [[g[0], g[1]]]
r = 0
gg = 0
for j in lr:
    while gg + x < j[0]:
        gg = gg + x
    r = r + j[1] - gg
    gg = j[1]
print(r)
