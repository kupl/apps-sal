n, m = list(map(int, input().split()))


if(m == 0):
    print(1, 0)
    print(n, 0)
    print(0, 0)
    print(n - 1, 0)
elif(n == 0):
    print(0, 1)
    print(0, m)
    print(0, 0)
    print(0, m - 1)
elif(n == 1 and m == 1):
    print(1, 1)
    print(0, 0)
    print(1, 0)
    print(0, 1)
elif(n == 1):
    print(0, 0)
    print(1, m)
    print(1, 0)
    print(0, m)
elif(m == 1):
    print(0, 0)
    print(n, 1)
    print(0, 1)
    print(n, 0)
else:

    if(n < m):
        a = pow(n**2 + m**2, 1 / 2) * 2 + max(n, m)
        b = pow((n - 1)**2 + m**2, 1 / 2) * 2 + pow(m**2 + n**2, 1 / 2)
        if(b > a):
            print(1, 0)
            print(n, m)
            print(0, 0)
            print(n - 1, m)
        else:
            print(0, 0)
            print(n, m)
            print(n, 0)
            print(0, m)
    else:
        a = pow(n**2 + m**2, 1 / 2) * 2 + max(n, m)
        b = pow((m - 1)**2 + n**2, 1 / 2) * 2 + pow(m**2 + n**2, 1 / 2)
        if(b > a):
            print(0, 1)
            print(n, m)
            print(0, 0)
            print(n, m - 1)
        else:
            print(0, 0)
            print(n, m)
            print(0, m)
            print(n, 0)
