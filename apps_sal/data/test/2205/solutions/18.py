from functools import reduce
from itertools import accumulate
from operator import xor
n = int(input())
res = reduce(xor, map(int, input().split()))
pre = [*accumulate(range(n + 1), xor)]
for i in range(1, n + 1):
    res ^= pre[n % i]
    if (n // i) & 1:
        res ^= pre[i - 1]
print(res)
