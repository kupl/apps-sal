from math import sqrt
from itertools import count, islice


def isPrime(n, p):
    j = int(sqrt(n))
    if p * p < n:
        j = p
    for i in range(2, j + 1):
        if n % i == 0:
            return False
    return True


p, y = list(map(int, input().split(' ')))
flag = 0
for i in range(y, p, -1):
    if isPrime(i, p):
        print(i)
        flag = 1
        break
if flag == 0:
    print(-1)
