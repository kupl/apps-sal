import math
from collections import defaultdict

n, k = map(int, input().split())
a = [int(i) for i in input().split()]
b = defaultdict(int)
for el in a:
    b[el] += 1
x = max(b.values())
v = math.ceil(x / k)
r = 0
for el in b.values():
    r += v * k - el
print(r)
