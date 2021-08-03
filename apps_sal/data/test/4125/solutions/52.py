from functools import reduce
n, x = map(int, input().split())
li = list(input().split())
li = [abs(int(a) - x) for a in li]


def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


a = reduce(gcd, li)
print(a)
