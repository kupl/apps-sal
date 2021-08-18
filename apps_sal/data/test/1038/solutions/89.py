for i in range(pow(10, 6)):
    pass

a, b = map(int, input().split())
if a % 2 == 0:
    if (b - a + 1) % 2 == 0:
        if (b - a + 1) % 4 == 0:
            print(0)
        else:
            print(1)
    else:
        if (b - a) % 4 == 0:
            print(0 ^ b)
        else:
            print(1 ^ b)
else:
    if (b - a) % 2 == 0:
        if (b - a) % 4 == 0:
            print(a ^ 0)
        else:
            print(a ^ 1)
    else:
        if (b - a - 1) % 4 == 0:
            print(0 ^ b ^ a)
        else:
            print(1 ^ b ^ a)
