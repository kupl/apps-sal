import math


def isPrime(n):
    if n < 2:
        return False
    else:
        divisors = []
        tem = []
        for p in range(1, math.ceil(n**(1 / 2) + 1)):
            if n % p == 0:
                divisors.append(p)

        for divisor in divisors:
            tem.append(n // divisor)

        divisors = list(set(sorted(divisors + tem)))

        if len(divisors) == 2:
            return True
        else:
            # print(divisors)
            return False


X = int(input())

while True:
    if isPrime(X):
        print(X)
        break
    else:
        X += 1
