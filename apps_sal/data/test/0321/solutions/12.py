import sys


def isprime(x):
    import math
    if x == 1:
        return True

    for i in range(2, math.ceil(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def __starting_point():
    cin = sys.stdin

    T = int(next(cin))
    for _ in range(T):
        n, m = list(map(int, next(cin).split()))

        if n - m == 1 and isprime(n + m):
            print('YES')
        else:
            print('NO')


__starting_point()
