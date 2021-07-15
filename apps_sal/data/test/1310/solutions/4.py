from operator import xor
from functools import reduce
n = int(input())
a = list(map(int, input().split()))
print(max(reduce(xor, a[i:j + 1]) for i in range(n) for j in range(i, n)))
