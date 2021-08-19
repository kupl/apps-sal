import sys

input = sys.stdin.readline

# N
# t1 x1 y1t1 x1 y1
# t2 x2 y2t2 x2 y2
# ⋮⋮
# tN xN yNtN xN yN
N = 3
x = [0 for i in range(N)]
y = [0 for i in range(N)]
c = [[0 for i in range(N)] for i in range(N)]

for i in range(N):
    c1, c2, c3 = map(int, input().split())
    c[i][0] = c1
    c[i][1] = c2
    c[i][2] = c3


x[0] = 0
for i in range(N):
    y[i] = c[0][i] - x[0]
x[1] = c[1][0] - y[0]
x[2] = c[2][0] - y[0]

flag = True
for i in range(N):
    for j in range(N):
        numx = x[i]
        numy = y[j]
        if not numx + numy == c[i][j]:
            flag = False
if flag:
    print("Yes")
else:
    print("No")
