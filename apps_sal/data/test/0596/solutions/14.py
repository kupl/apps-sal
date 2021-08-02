# -------------------------------------------------------------------------------
# Name:        Codeforces
# Author:      Gogol2

# -------------------------------------------------------------------------------

m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def leap(yy):
    if ((yy % 400 == 0 or (yy % 4 == 0 and yy % 100))):
        return 366
    else:
        return 365


def main():

    y1, m1, d1 = list(map(int, input().split(':')))
    y2, m2, d2 = list(map(int, input().split(':')))
    a = d1
    b = d2
    for i in range(0, y1):
        a = a + leap(i)
    for i in range(0, y2):
        b = b + leap(i)
    for i in range(m1 - 1):
        a = a + m[i]
        if (leap(y1) == 366 and i == 1):
            a = a + 1
    for i in range(m2 - 1):
        b = b + m[i]
        if (leap(y2) == 366 and i == 1):
            b = b + 1
    print(abs(a - b))


def __starting_point():
    main()


__starting_point()
