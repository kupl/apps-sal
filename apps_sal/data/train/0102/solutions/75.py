a = int(input())
for i in range(a):
    n = int(input())
    b = 1
    k = 1
    d = 0
    while b * k <= n:
        if k == 9:
            k = 0
            b *= 10
            b += 1
        d += 1
        k += 1
    print(d)
