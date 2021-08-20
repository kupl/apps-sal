from math import log2


def minpow2(x, y):
    return int(log2(x // y))


(a, b) = list(map(int, input().split()))
while a > 0 and b > 0:
    if a >= 2 * b:
        a = a % (2 * b)
        continue
    elif b >= 2 * a:
        b = b % (2 * a)
        continue
    else:
        break
print(a, b)
