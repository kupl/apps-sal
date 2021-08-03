from collections import Counter
from itertools import accumulate
from bisect import bisect_right


def factor(n):
    res = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            res.append(i)
            n //= i
    if n > 1:
        return res + [n]
    else:
        return res


num = [i for i in range(1, 65)]
num = list(accumulate(num))

N = int(input())
primes = Counter(factor(N))
ans = 0
for v in list(primes.values()):
    ans += bisect_right(num, v)
print(ans)
