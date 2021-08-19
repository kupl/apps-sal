import heapq
from collections import defaultdict
# python template for atcoder1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

X, Y = list(map(int, input().split()))


def primeFact_set(n):
    factors = set()
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
            if i <= Y:
                factors.add(i)
        else:
            i += 1
    if n > 1 and n <= Y:
        factors.add(n)
    return factors


X_prime = primeFact_set(X)
MOD = 10**9 + 7
ans = 1
for p in X_prime:
    tmp = p
    while tmp <= Y:
        div = Y // tmp
        ans *= pow(p, div, MOD)
        ans %= MOD
        tmp *= p
print(ans)
