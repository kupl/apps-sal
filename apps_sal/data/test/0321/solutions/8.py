from math import sqrt
from itertools import count, islice


def isPrime(n):
    return n > 1 and all((n % i for i in islice(count(2), int(sqrt(n) - 1))))


t = int(input())
for i in range(t):
    (a, b) = map(int, input().split())
    ans = False
    if a - b == 1:
        x = a + b
        ans = isPrime(x)
    if ans:
        print('YES')
    else:
        print('NO')
