import math


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all((n % i for i in range(3, int(math.sqrt(n)) + 1, 2)))


n = int(input())
m = 1
while is_prime(n * m + 1):
    m += 1
print(m)
