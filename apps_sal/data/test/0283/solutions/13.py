import math


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


n = int(input())
for i in range(1, 1001):
    if not is_prime(n * i + 1):
        print(i)
        break
