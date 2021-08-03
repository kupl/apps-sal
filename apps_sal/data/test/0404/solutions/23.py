import math


def divisorGenerator(n):
    l_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                l_divisors.append(n / i)
    for divisor in reversed(l_divisors):
        yield divisor


n = int(input())
print(len(list(divisorGenerator(n))))
