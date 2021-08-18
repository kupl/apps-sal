n, z, w = list(map(int, input().split()))
a = list(map(int, input().split()))

if n >= 2:

    dp_x = [abs(a[-1] - a[i]) for i in range(n)]
    dp_y = [abs(a[-1] - a[i]) for i in range(n)]

    for i in reversed(list(range(n - 1))):
        for j in range(i):
            dp_x[j] = min(dp_x[j], dp_y[i])
            dp_y[j] = max(dp_y[j], dp_x[i])

    print((max(abs(a[-1] - w), max(dp_x))))
else:
    print((abs(a[-1] - w)))
