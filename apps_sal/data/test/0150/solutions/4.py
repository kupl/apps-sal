import math


def isprime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
if isprime(n):
    print(1)
elif n % 2 == 0:
    print(2)
elif n % 2 == 1:
    if isprime(n - 2):
        print(2)
    else:
        print(3)
