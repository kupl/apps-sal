from math import *


def IsPrime(n):
    for i in range(2, ceil(sqrt(n)) + 1):
        if not (n % i):
            return False
    return True


n = int(input())
if IsPrime(n) or n == 2:
    print(1)
elif (not n % 2):
    print(2)
elif IsPrime(n - 2):
    print(2)
else:
    print(3)
