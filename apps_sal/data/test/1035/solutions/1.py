import math


def factrize(num):
    factor = {}
    div = 2
    s = int(num**0.5) + 1
    while div < s:
        div_cnt = 0
        while num % div == 0:
            div_cnt += 1
            num //= div
        if div_cnt != 0:
            factor[div] = div_cnt
        div += 1
    if num > 1:
        factor[num] = 1
    return factor


a, b = map(int, input().split())
g = math.gcd(a, b)
print(len(factrize(g)) + 1)
