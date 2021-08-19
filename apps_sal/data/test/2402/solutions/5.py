import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


def solve():
    (n, x, y) = list(map(int, input().split()))
    if x > y:
        (x, y) = (y, x)
    x1 = min(x - 1, max(0, n - y - 1))
    y1 = min(y - 1, max(0, n - x - 1))
    x_left = x - 1 - x1
    y_left = y - 1 - y1
    mi = 1 + max(x_left, y_left)
    x1 = min(x - 1, n - y)
    x2 = x - 1 - x1
    y1 = min(y - 1, n - x)
    y2 = y - 1 - y1
    ma = x1 + y1 + min(x2, y2) + 1
    print(mi, ma)


t = int(input())
for i in range(t):
    solve()
