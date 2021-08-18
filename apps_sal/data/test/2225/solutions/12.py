from operator import or_, xor
import sys

n, m = map(int, input().split())
t = [list(map(int, input().split()))]

for i in range(n):
    t += [[(or_, xor)[i & 1](t[i][j], t[i][j + 1]) for j in range(0, len(t[i]), 2)]]


for s in sys.stdin:
    p, b = s.split()
    p = int(p) - 1
    t[0][p] = int(b)
    for j in range(n):
        p = int(p / 2)
        t[j + 1][p] = (or_, xor)[j & 1](t[j][int(p * 2)], t[j][int(p * 2) + 1])
    sys.stdout.write(str(t[-1][0]) + '\n')
