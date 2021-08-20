try:
    from string_source import string_source
    source = string_source('2\n2 6')
except ImportError:
    source = input
from collections import Counter


def two_factors(n):
    if n == 0:
        return 0
    f = 0
    while n % 2 == 0:
        f += 1
        n //= 2
    return f


def f(numbers):
    twos = list(map(two_factors, numbers))
    m = max(list(Counter(twos).items()), key=lambda x: x[1])[0]
    erased = [n for (n, t) in zip(numbers, twos) if t != m]
    return (len(erased), erased)


source()
(n, erased) = f(list(map(int, source().split(' '))))
print(n)
print(' '.join(map(str, erased)))
