import math


def solve():
    n = int(input())
    m = int(math.sqrt(n))
    while n % m != 0:
        m -= 1
    return str(m) + ' ' + str(int(n / m))


print(solve())
