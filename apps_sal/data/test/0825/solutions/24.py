import math
N = int(input())


def prime_decomposition(x):
    i = 2
    ls = []
    while i * i <= x:
        while x % i == 0:
            x /= i
            ls.append(i)
        i += 1
    if x > 1:
        ls.append(int(x))
    return ls


def counter(n):
    i = 1
    while n > 0.5 * (i + 1) * (i + 2) - 1:
        i += 1
    return i


cnt = 0
numbers = prime_decomposition(N)
set_number = set(numbers)

for i in set_number:
    cnt += counter(numbers.count(i))

print(cnt)
