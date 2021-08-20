(n, d, h) = map(int, input().split())
if d / 2 > h or n < d + 1 or (h == d == 1 and n > 2):
    print(-1)
else:
    p = 1
    for i in range(2, h + 2):
        print(i - 1, i)
        p += 1
    if d == h and n > d + 1:
        print(2, p + 1)
        p += 1
        for i in range(p + 1, n + 1):
            print(2, i)
            p += 1
    elif d - h > 0:
        print(1, p + 1)
        p += 1
        for i in range(p + 1, p + d - h):
            print(i - 1, i)
            p += 1
        for i in range(p + 1, n + 1):
            print(1, i)
            p += 1
