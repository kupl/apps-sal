import math

p, y = list(map(int, input().split()))


def isPrime(p, n):
    i = 2
    while i <= math.sqrt(n) and i <= p:
        if n % i == 0:
            return False
        i += 1
    return True


i = y
ans = -1
while i > p:
    if isPrime(p, i):
        ans = i
        break
    i -= 1

print(ans)
