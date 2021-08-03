import math


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def div(n):
    cnt = 0
    temp = n
    for i in range(2, int(math.sqrt(n)) + 1):
        if temp % i == 0:
            while temp % i == 0:
                temp //= i
            cnt += 1
    if temp != 1:
        cnt += 1
    return cnt + 1


a, b = map(int, input().split())
print(div(gcd(a, b)))
