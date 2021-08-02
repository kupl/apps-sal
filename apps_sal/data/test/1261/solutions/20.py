from math import log


def func(n, i):
    if n == 3:
        return (str(1 * i) + ' ') + (str(1 * i) + ' ') + (str(3 * i))
    if n % 2 == 0:
        odd = n // 2
    else:
        odd = n // 2 + 1
    q = 1 * i
    s = (str(q) + ' ') * odd
    return s


n = int(input())
if n == 3:
    s = '1 1 3'
else:
    s = ''
    z = 1
    while(n > 0):
        s = s + func(n, z)
        z = z * 2
        if n == 3:
            break
        if n % 2 == 0:
            odd = n // 2
        else:
            odd = n // 2 + 1
        n = n - odd
print(s)
