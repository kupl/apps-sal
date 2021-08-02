from math import sqrt, ceil


def mindiv(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    div, inc = 5, 2
    while div < ceil(sqrt(n)) + 1:
        if n % div == 0:
            return div
        div += inc
        inc = 6 - inc
    return n


n = int(input())
m = mindiv(n)
while n % m == 0 and n > m:
    n = n / m
print(1 if n > m else m)
