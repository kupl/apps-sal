n, m, k, x, y = [int(x) for x in input().split()]
maxi = 0
mini = 0
ser = 0
if (n == 1):
    if (k % m == 0):
        maxi = k // m
        mini = k // m
        ser = k // m
    else:
        maxi = k // m + 1
        mini = k // m
        if (y <= (k % m)):
            ser = maxi
        else:
            ser = mini
    print(maxi, mini, ser)
    return
if (n == 2):
    if (k % (2 * m) == 0):
        maxi = k // (2 * m)
        mini = k // (2 * m)
        ser = k // (2 * m)
    else:
        maxi = k // (2 * m) + 1
        mini = k // (2 * m)
        if ((x - 1) * m + y <= (k % (2 * m))):
            ser = maxi
        else:
            ser = mini
    print(maxi, mini, ser)
    return
if (k < (2 * n - 2) * m):
    if (k < n * m):
        maxi = 1
        mini = 0
        if ((x - 1) * m + y <= k):
            ser = 1
        else:
            ser = 0
    elif (k == n * m):
        maxi = 1
        mini = 1
        ser = 1
    else:
        maxi = 2
        mini = 1
        if ((x == 1) or (x == n)):
            ser = 1
        else:
            if (k - n * m >= y + (n - 1 - x) * m):
                ser = 2
            else:
                ser = 1
    print(maxi, mini, ser)
else:
    mini = k // ((2 * n - 2) * m)
    maxi = 2 * mini
    if (k % ((2 * n - 2) * m) > m):
        if (k % ((2 * n - 2) * m) > m * n):
            maxi += 2
            mini += 1
        else:
            maxi += 1
        if (k % ((2 * n - 2) * m) == m * n):
            mini += 1
    if (x == 1):
        ser = k // ((2 * n - 2) * m)
        if (k % ((2 * n - 2) * m) >= y):
            ser += 1
    elif (x == n):
        ser = k // ((2 * n - 2) * m)
        if (k % ((2 * n - 2) * m) >= y + (n - 1) * m):
            ser += 1
    else:
        if (k % ((2 * n - 2) * m) <= n * m):
            if ((x - 1) * m + y <= k % ((2 * n - 2) * m)):
                ser = (k // ((2 * n - 2) * m)) * 2 + 1
            else:
                ser = (k // ((2 * n - 2) * m)) * 2
        else:
            ser = (k // ((2 * n - 2) * m)) * 2 + 1
            if (k % ((2 * n - 2) * m) - n * m >= (n - 1 - x) * m + y):
                ser += 1
    print(maxi, mini, ser)
