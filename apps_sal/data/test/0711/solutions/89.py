from math import floor, sqrt
from collections import defaultdict
(N, M) = map(int, input().split())
d = defaultdict(int)
for i in range(2, floor(sqrt(M)) + 1):
    while M % i == 0:
        d[i] += 1
        M //= i
if M != 1:
    d[M] += 1


def comb(n, k):
    if k == 0:
        return 1
    return comb(n - 1, k - 1) * n // k


ans = 1
for e in d.values():
    ans *= comb(N + e - 1, e)
print(ans % (10 ** 9 + 7))
