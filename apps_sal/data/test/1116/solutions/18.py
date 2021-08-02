n = int(input())


def m(x, y):
    a = max(x, y)
    b = min(x, y)
    while a != b:
        c = a % b
        a = b
        b = c
        if c == 0:
            break
    return a


for i in range(n):
    r, b, k = [int(x) for x in input().split(' ')]
    a = m(r, b)
    x = max(r, b)
    y = min(r, b)
    if (2 * x) % y != 0:
        if x >= (k - 1) * y + 2 * a:
            print('REBEL')
        else:
            print('OBEY')
    elif x % y == 0:
        if x >= (k + 1) * y:
            print('REBEL')
        else:
            print('OBEY')
    else:
        if x >= k * y + a:
            print('REBEL')
        else:
            print('OBEY')
