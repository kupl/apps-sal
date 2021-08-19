t = int(input())
for i in range(t):
    (x, y, p, q) = [int(i) for i in input().split()]
    if p == 0:
        if x == 0:
            print(0)
        else:
            print(-1)
        continue
    l = 0
    r = 10000000000
    while l < r:
        t = (l + r) // 2
        c1 = p * t - x
        c2 = q * t - y - c1
        if c1 >= 0 and c2 >= 0:
            r = t
        else:
            l = t + 1
    if r == 10000000000:
        print(-1)
    else:
        print(q * l - y)
