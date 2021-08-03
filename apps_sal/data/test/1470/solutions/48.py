x = int(input())

if x <= 6:
    print((1))
elif x <= 11:
    print((2))
else:
    if x % 11 == 0:
        print((2 * (x // 11)))
    else:
        if (x - (x // 11) * 11) <= 6:
            print((2 * (x // 11) + 1))
        elif (x - (x // 11) * 11) <= 11:
            print((2 * (x // 11) + 2))
