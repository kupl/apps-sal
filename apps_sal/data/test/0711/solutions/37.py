import math
from collections import defaultdict
N, M = list(map(int, input().split(' ')))
if M == 1:
    print(1)  # a_i = 1 for all i
    return
# prime factorization of M
fact = defaultdict(int)
for i in range(2, int(math.sqrt(M) + 1)):
    while M % i == 0:
        M //= i
        fact[i] += 1
if M != 1:
    # M is prime
    fact[M] = 1
# calculate answer
answer = 1
mod = 10**9 + 7
for f in fact.values():
    # calc combination(f + N - 1, f) = (f + N - 1) * ... * N / f!
    numerator = 1
    denominator = 1
    for i in range(f):
        numerator *= (N + i)
        denominator *= (i + 1)
    answer *= (numerator // denominator)
    answer %= mod
print(answer)
