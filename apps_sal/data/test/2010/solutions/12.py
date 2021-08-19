import sys

n, m = [int(x) for x in sys.stdin.readline().split()]
a = [int(x) for x in sys.stdin.readline().split()]
increase = 0

for i in range(m):
    op = [int(x) for x in sys.stdin.readline().split()]
    t = op[0]  # type of operation
    if t == 1:
        v = op[1]
        x = op[2]
        a[v - 1] = x - increase
    elif t == 2:
        y = op[1]
        increase += y
    elif t == 3:
        q = op[1]
        print(a[q - 1] + increase)
