from functools import reduce
from operator import xor
a = [*map(int, input())]
b = [*map(int, input())]
n = len(b)
curr = reduce(xor, b)
curr ^= reduce(xor, a[:n])
res = int(curr & 1 == 0)
for i in range(n, len(a)):
    curr ^= a[i] ^ a[i - n]
    res += curr & 1 == 0
print(res)
