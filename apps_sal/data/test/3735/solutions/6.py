from math import log10, ceil


def sumdigs(n):
    return sum(map(int, str(n)))


n = int(input())
tens = int(log10(n))
nines = tens * 9
print(nines + sumdigs(n - (10 ** tens - 1)))
