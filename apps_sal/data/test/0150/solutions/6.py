import math

def isprime(n):
    if n == 2:
        return True

    sq = math.ceil(n ** 0.5) + 1
    for i in range(2, sq):
        if n % i == 0:
            return False
    return True

def solve(n):
    if isprime(n):
        return 1
    if n%2 == 0:
        return 2
    if isprime(n - 2):
        return 2
    return 3

n = int(input())
print(solve(n))

