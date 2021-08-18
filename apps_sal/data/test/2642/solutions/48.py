
from collections import Counter
from math import gcd

n = int(input())
counter = Counter()
for i in range(n):
    a, b = list(map(int, input().split()))
    if b < 0:
        a, b = -a, -b
    elif b == 0:
        a = abs(a)
    if not a == b == 0:
        g = gcd(a, b)
        a //= g
        b //= g
    counter[(a, b)] += 1

modulus = 1000000007

vs = set(counter)
vs.update((b, -a) for a, b in counter if a <= 0)
vs = [(a, b) for a, b in vs if a > 0]

ncomb = 1
for a, b in vs:
    n1 = counter[(a, b)]
    n2 = counter[(-b, a)]
    m = pow(2, n1, modulus) + pow(2, n2, modulus) - 1
    ncomb = ncomb * m % modulus

ncomb -= 1

ncomb += counter[(0, 0)]

print((ncomb % modulus))
