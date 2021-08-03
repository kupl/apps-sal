x, k, d = map(int, input().split())

if x >= 0:
    a = abs(x // d)
    if a <= k:
        if (k - a) % 2 == 0:
            print(abs(x - a * d))
        else:
            print(abs(x - (a + 1) * d))
    else:
        print(abs(x - k * d))
else:
    if x % d == 0:
        a = abs(x // d)
    else:
        a = abs(x // d + 1)

    if a <= k:
        if (k - a) % 2 == 0:
            print(abs(x + a * d))
        else:
            print(abs(x + (a + 1) * d))
    else:
        print(abs(x + k * d))
