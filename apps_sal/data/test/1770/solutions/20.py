import math
n = int(input())
for i in range(n):
    c1, c2, c3 = 1e11, 1e11, 1e11
    n, x, y, d = list(map(int, input().split()))
    if (abs(y - x) % d == 0):
        c3 = abs((y - x)) // d
    else:
        if (abs(y - 1) % d == 0):
            c1 = math.ceil((x - 1) / d) + ((y - 1) // d)
        if (abs(n - y) % d == 0):
            c2 = math.ceil((n - x) / d) + (abs((y - n)) // d)
    m = min(c1, c2, c3)
    if (m == 1e11):
        print(-1)
    else:
        print(m)
