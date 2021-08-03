from math import sqrt
from itertools import count, islice

n = int(input())


def isPrime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


def eval_(a, b):
    if abs(a - b) != 1:
        return "NO"
    result = isPrime(a + b)
    if result:
        return "YES"
    else:
        return "NO"


for i in range(n):
    (a, b) = [int(x) for x in input().split()]
    print(eval_(a, b))
