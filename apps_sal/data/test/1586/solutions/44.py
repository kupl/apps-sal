n = int(input())

if n % 2 == 0:
    n5 = 1
    y = 10
    c = []

    while y <= n:
        c.append(n // y)
        if len(c) > 1:
            c[-2] -= c[-1]
        y *= 5

    cnt = 0
    for i in range(len(c)):
        cnt += c[i] * (i + 1)

    print(cnt)
else:
    print(0)
