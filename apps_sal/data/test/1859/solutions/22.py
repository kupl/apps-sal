from math import sqrt


def kek(n):
    if n == 2:
        return 2
    for i in range(2, int(sqrt(n)) + 2):
        if n % i == 0:
            return i
    return n


n = int(input())
k = 0
while n > 0:
    if n % 2 == 0:
        k += n // 2
        break
    k += 1
    n -= kek(n)
print(k)
