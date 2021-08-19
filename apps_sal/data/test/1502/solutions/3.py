n = int(input(''))
a = [0, 0, 0, 0]
a[0] = n % 2
n = n // 2
a[1] = n % 2
n = n // 2
a[2] = n % 2
n = n // 2
a[3] = n % 2


def intnot(x):
    return 0 if x == 1 else 1


a[3] = intnot(a[3])
if a[3] == 1:
    a[2] = intnot(a[2])
if a[3] + a[2] == 2:
    a[1] = intnot(a[1])
if a[3] + a[2] + a[1] == 3:
    a[0] = intnot(a[0])
n = 8 * a[3] + 4 * a[2] + 2 * a[1] + a[0]
print(n)
