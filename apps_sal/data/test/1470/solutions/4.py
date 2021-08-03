x = int(input())

if 7 <= x <= 11:
    print(2)
elif x <= 6:
    print(1)
else:
    a, b = divmod(x, 11)
    if b == 0:
        print(2 * a)
    else:
        if b <= 6:
            print(2 * a + 1)
        else:
            print(2 * a + 2)
