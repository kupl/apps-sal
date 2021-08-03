from math import sqrt, floor

n = input()


def is_square(n):
    f = floor(sqrt(n))
    return f * f == n or (f + 1) * (f + 1) == n


def min_to_square(d, n):
    if len(n) == 1:
        return d if is_square(int(n)) else 100

    if n[0] == '0':
        return 100

    if (n[0] != '0' and is_square(int(n))) or n == '0':
        return d

    m = min([min_to_square(d + 1, n[:i] + n[i + 1:]) for i in range(len(n))])

    return m


def mts(n):
    min_ = 100

    for i in range(1, 2**(len(n))):
        s = "{0:b}".format(i).zfill(len(n))

        newn = ''.join([n[i] for i in range(len(n)) if s[i] == '1'])

        if is_square(int(newn)) and newn[0] != '0':
            min_ = min(min_, sum(1 for c in s if c == '0'))

    return min_


print(mts(n) if mts(n) < 100 else -1)
