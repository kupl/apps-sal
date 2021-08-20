import math
import collections


def prime_factor(n):
    ass = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            ass.append(i)
            n = n // i
    if n != 1:
        ass.append(n)
    return ass


n = int(input())
nums = list(map(int, input().split(' ')))
g = nums[0]
for i in range(1, n):
    g = math.gcd(g, nums[i])
primes = prime_factor(g)
c = collections.Counter(primes)
out = 1
for val in c.values():
    out *= val + 1
print(out)
