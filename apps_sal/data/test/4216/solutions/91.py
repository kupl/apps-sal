import math


def f(a, b: int) -> int:
    alen = len(str(a))
    blen = len(str(b))
    if alen > blen:
        return alen
    else:
        return blen


n = int(input())
max = int(math.sqrt(n))
fmin = len(str(n))

for i in range(1, max+1):
    if n % i == 0:
        tmp = f(i, int(n/i))
        if tmp < fmin:
            fmin = tmp
print(fmin)
