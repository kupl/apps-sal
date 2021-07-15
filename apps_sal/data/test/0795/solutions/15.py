from math import gcd


def theorem(n):
    i = 1
    result = 0
    while i * i <= n:
        j = i + 1
        while i * i + j * j <= n:
            c, a, b = i * i + j * j, j * j - i * i, 2 * i * j
            if gcd(i, j) == 1 and (i % 2 != 0 and j % 2 == 0 or i % 2 == 0 and j % 2 != 0):
                result += n // c
            j += 1
        i += 1
    return result


print(theorem(int(input())))


