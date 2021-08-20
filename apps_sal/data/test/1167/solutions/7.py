from math import ceil
t = int(input())
for i in range(t):
    (a, b, c, d, k) = [int(x) for x in input().split()]
    x = ceil(a / c)
    y = ceil(b / d)
    if x + y <= k:
        print(x, y)
    else:
        print(-1)
