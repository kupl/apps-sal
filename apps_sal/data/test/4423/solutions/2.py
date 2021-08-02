import re
n = int(input())
R = []
for i in range(n):
    S, P = input().split()
    R.append((S, int(P), int(i + 1)))

Point = []
for j in range(n):
    Point.append(R[j][0])
Point = list(sorted(set(Point)))
Point
SR = sorted(R, key=lambda x: (x[0], -int(x[1])))
for k in range(n):
    print(SR[k][2])
pass
