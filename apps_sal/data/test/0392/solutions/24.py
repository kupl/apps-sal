import sys
from math import ceil, sqrt


def factor(n):
    if n <= 1: return []
    prime = next((x for x in range(2, ceil(sqrt(n)) + 1) if n % x == 0), n)
    return [prime] + factor(n // prime)


n = int(sys.stdin.readline().rstrip('\n'))
setprimes = set(factor(n))
cumul = 1
for p in setprimes:
    cumul *= p
print(cumul)
