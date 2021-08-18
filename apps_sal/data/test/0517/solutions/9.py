import math
n, d, h = list(map(int, input().split()))
if (h < math.ceil(d / 2)) or ((n > 2) and (d < 2)):
    print(-1)
else:
    for i in range(h):
        print(i + 1, i + 2)
    if (d - h > 0):
        print(1, h + 2)
    for i in range(h + 2, d + 1):
        print(i, i + 1)
    add_to = 1
    if (d == h):
        add_to = 2
    for i in range(d + 2, n + 1):
        print(add_to, i)
