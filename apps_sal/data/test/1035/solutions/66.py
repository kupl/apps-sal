import math


def using_sqrt(k):
    factor = 0

    if k % 2 == 0 and k != 2:
        return False

    for divisor in range(2, math.floor(math.sqrt(k)) + 1):
        if k % divisor == 0:
            factor += 1

    if factor == 0:
        return True
    else:
        return False


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    divisors.sort()
    return divisors


def make_codivisors(n):
    divisors = []
    n0divisors = make_divisors(n[0])
    n0len = len(n0divisors)
    for i in n0divisors:
        for j in range(1, len(n)):
            if n[j] % i != 0:
                break
            if j == len(n) - 1:
                divisors.append(i)

    return divisors


a, b = map(int, input().split())
div = make_codivisors([a, b])
ans = 0
for i in div:
    if i == 1:
        ans += 1
    else:
        if using_sqrt(i):
            ans += 1
print(ans)
