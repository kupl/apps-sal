x = int(input())
if x == 1:
    print(1)
    print(1)
elif x == 2:
    print(1)
    print(1)
elif x == 3:
    print(2)
    print(1, 3)
else:
    if x % 2 == 0:
        t = [0] * x
        for i in range(x // 2):
            t[2 * i + 1] = i + 1
        for i in range(x // 2):
            t[2 * i] = i + x // 2 + 1
        print(x)
        print(' '.join([str(x) for x in t]))
    else:
        t = [0] * x
        for i in range(x // 2):
            t[2 * i + 1] = i + 1
        for i in range(x // 2):
            t[2 * i] = i + x // 2 + 1
        print(x)
        t[-1] = x
        print(' '.join([str(x) for x in t]))
