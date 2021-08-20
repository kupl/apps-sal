t = int(input())
while t > 0:
    t = t - 1
    l = input().split()
    a = int(l[0])
    b = int(l[1])
    c = int(l[2])
    d = int(l[3])
    if a != 0:
        if (a + b) % 2 == 1:
            print('Ya', end=' ')
        else:
            print('Tidak', end=' ')
    elif d >= 1 and (a + b) % 2 == 1:
        print('Ya', end=' ')
    else:
        print('Tidak', end=' ')
    if b != 0:
        if (a + b) % 2:
            print('Ya', end=' ')
        else:
            print('Tidak', end=' ')
    elif c >= 1 and (a + b) % 2 == 1:
        print('Ya', end=' ')
    else:
        print('Tidak', end=' ')
    if c != 0:
        if (a + b) % 2 == 0:
            print('Ya', end=' ')
        else:
            print('Tidak', end=' ')
    elif b >= 1 and (a + b) % 2 == 0:
        print('Ya', end=' ')
    else:
        print('Tidak', end=' ')
    if d != 0:
        if (a + b) % 2 == 0:
            print('Ya', end=' ')
        else:
            print('Tidak', end=' ')
    elif a >= 1 and (a + b) % 2 == 0:
        print('Ya', end=' ')
    else:
        print('Tidak', end=' ')
    print()
