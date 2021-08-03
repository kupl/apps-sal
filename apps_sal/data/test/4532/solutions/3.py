import math
t = int(input())
for _ in range(t):
    n, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    ma = -1
    d = {}
    for i in a:
        if i % k == 0:
            continue
        r = i % k
        r = k - r
        if r not in d:
            d[r] = 0
        d[r] += 1
        ma = max(ma, r + ((d[r] - 1) * k))
    print(ma + 1)
