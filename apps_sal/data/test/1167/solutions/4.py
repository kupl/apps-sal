from math import ceil

for __ in range(int(input())):
    a, b, c, d, k = list(map(int, input().split()))
    x = ceil(a / c)
    y = ceil(b / d)
    if x + y > k:
        print(-1)
    else:
        print(x, y)
