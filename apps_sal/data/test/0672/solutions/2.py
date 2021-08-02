import math
import collections


def multipliers(x):

    divisors = []
    divisor = 2
    stop = math.sqrt(x)
    while x != 1 and divisor <= stop:

        if x % divisor == 0:

            x //= divisor
            divisors.append(divisor)

        else:

            divisor += 1

    if x != 1:

        divisors.append(x)

    return divisors


def count(muls, bound, viewed=None, x=1):

    viewed = viewed or set()
    for i, mul in enumerate(muls):

        nx = x * mul
        if nx not in viewed:

            viewed.add(nx)
            if nx > bound:

                yield 1

            yield from count(muls[:i] + muls[i + 1:], bound, viewed, nx)


a, b = list(map(int, input().split()))
# a, b = 4, 0
if a == b:

    print("infinity")

elif b > a or a == 0:

    print(0)

elif (a, b) == (1, 0):

    print(1)

else:

    muls = multipliers(a - b)
    r = sum(count(muls, b))
    print(r if b else r + 1)
