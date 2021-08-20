import math
for _ in range(int(input())):
    (a, b, c, d, k) = list(map(int, input().split(' ')))
    tot = 0
    a = math.ceil(a / c)
    b = math.ceil(b / d)
    if a + b <= k:
        print(a, b)
    else:
        print(-1)
