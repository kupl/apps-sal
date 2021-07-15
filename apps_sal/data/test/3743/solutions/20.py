import math


def p(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return i
    else:
        return x


def r(x):
    if round(x) - x < 0.5:
        return round(x)
    else:
        return round(x) - 1


n = int(input())
if n == 1:
    print(1)
else:
    m = p(n)
    d = math.log(n, m)
    if m**r(d) == n:
        print(m)
    else:
        print(1)

