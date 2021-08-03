A = input().split()
n = int(A[0])
m = int(A[1])
k = int(A[2])


def ans(e):
    final = 1
    for i in range(0, e):
        final = (final * 2) % 1000000007
    return(final)


if m == 1:
    if k == 1:
        print(1)
    elif k == -1:
        if n % 2 == 0:
            print(0)
        elif n % 2 == 1:
            print(1)
elif n == 1:
    if k == 1:
        print(1)
    elif k == -1:
        if m % 2 == 0:
            print(0)
        elif m % 2 == 1:
            print(1)
else:
    if k == 1:
        e1 = (m - 1) % 1000000006
        e2 = (n - 1) % 1000000006
        e = (e1 * e2) % 1000000006
        print(pow(2, e, 1000000007))
    elif k == -1:
        if m % 2 != n % 2:
            print(0)
        else:
            e1 = (m - 1) % 1000000006
            e2 = (n - 1) % 1000000006
            e = (e1 * e2) % 1000000006
            print(pow(2, e, 1000000007))
