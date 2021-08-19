import sys
t = int(sys.stdin.readline())
for i in range(t):
    (d, v, l, r) = list(map(int, sys.stdin.readline().strip().split()))
    x = int(d / v)
    y = int(r / v) - int((l - 1) / v)
    if l == r and l % v == 0:
        y = 1
    print(x - y)
