from sys import stdin


def main():
    f1 = [1, 1, 1]
    f2 = [1, 1, 1]
    f3 = [1, 1, 1]
    a = str(stdin.readline()).split()
    b = str(stdin.readline()).split()
    c = str(stdin.readline()).split()
    for i in range(3):
        a[i] = int(a[i])
        b[i] = int(b[i])
        c[i] = int(c[i])
    if (a[0] % 2 != 0):
        if (f1[0] == 0):
            f1[0] = 1
        else:
            f1[0] = 0
        if (f2[0] == 0):
            f2[0] = 1
        else:
            f2[0] = 0
        if (f1[1] == 0):
            f1[1] = 1
        else:
            f1[1] = 0
    if (a[1] % 2 != 0):
        if (f1[0] == 0):
            f1[0] = 1
        else:
            f1[0] = 0
        if (f1[1] == 0):
            f1[1] = 1
        else:
            f1[1] = 0
        if (f2[1] == 0):
            f2[1] = 1
        else:
            f2[1] = 0
        if (f1[2] == 0):
            f1[2] = 1
        else:
            f1[2] = 0
    if (a[2] % 2 != 0):
        if (f1[1] == 0):
            f1[1] = 1
        else:
            f1[1] = 0
        if (f1[2] == 0):
            f1[2] = 1
        else:
            f1[2] = 0
        if (f2[2] == 0):
            f2[2] = 1
        else:
            f2[2] = 0
    if (b[0] % 2 != 0):
        if (f1[0] == 0):
            f1[0] = 1
        else:
            f1[0] = 0
        if (f2[0] == 0):
            f2[0] = 1
        else:
            f2[0] = 0
        if (f3[0] == 0):
            f3[0] = 1
        else:
            f3[0] = 0
        if (f2[1] == 0):
            f2[1] = 1
        else:
            f2[1] = 0
    if (b[1] % 2 != 0):
        if (f2[0] == 0):
            f2[0] = 1
        else:
            f2[0] = 0
        if (f1[1] == 0):
            f1[1] = 1
        else:
            f1[1] = 0
        if (f2[1] == 0):
            f2[1] = 1
        else:
            f2[1] = 0
        if (f3[1] == 0):
            f3[1] = 1
        else:
            f3[1] = 0
        if (f2[2] == 0):
            f2[2] = 1
        else:
            f2[2] = 0
    if (b[2] % 2 != 0):
        if (f2[1] == 0):
            f2[1] = 1
        else:
            f2[1] = 0
        if (f1[2] == 0):
            f1[2] = 1
        else:
            f1[2] = 0
        if (f2[2] == 0):
            f2[2] = 1
        else:
            f2[2] = 0
        if (f3[2] == 0):
            f3[2] = 1
        else:
            f3[2] = 0
    if (c[0] % 2 != 0):
        if (f2[0] == 0):
            f2[0] = 1
        else:
            f2[0] = 0
        if (f3[0] == 0):
            f3[0] = 1
        else:
            f3[0] = 0
        if (f3[1] == 0):
            f3[1] = 1
        else:
            f3[1] = 0
    if (c[1] % 2 != 0):
        if (f3[0] == 0):
            f3[0] = 1
        else:
            f3[0] = 0
        if (f2[1] == 0):
            f2[1] = 1
        else:
            f2[1] = 0
        if (f3[1] == 0):
            f3[1] = 1
        else:
            f3[1] = 0
        if (f3[2] == 0):
            f3[2] = 1
        else:
            f3[2] = 0
    if (c[2] % 2 != 0):
        if (f3[1] == 0):
            f3[1] = 1
        else:
            f3[1] = 0
        if (f2[2] == 0):
            f2[2] = 1
        else:
            f2[2] = 0
        if (f3[2] == 0):
            f3[2] = 1
        else:
            f3[2] = 0
    d = str(f1[0])
    e = str(f1[1])
    f = str(f1[2])
    g = str(f2[0])
    h = str(f2[1])
    i = str(f2[2])
    j = str(f3[0])
    k = str(f3[1])
    l = str(f3[2])
    print(d + e + f)
    print(g + h + i)
    print(j + k + l)


main()
