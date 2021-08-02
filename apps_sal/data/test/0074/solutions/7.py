import math


def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def decomposition(even):
    if even == 4: return 2, 2
    for i in range(even - 3, int(math.sqrt(even)) - 1, -2):
        if is_prime(i) and is_prime(even - i):
            return i, even - i


n = int(input())
if is_prime(n):
    print(1)
    print(n)
else:
    for i in range(n, 3, -2):
        if is_prime(i):
            if n - i == 2:
                print(2)
                print(i, 2)
                break
            else:
                print(3)
                print(i, *decomposition(n - i))
                break
