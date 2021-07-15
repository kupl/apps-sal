import math
from collections import defaultdict
import numpy as np
n = int(input())
dic = defaultdict(lambda : 0)
for i in range(2, n + 1):
    sqrt = math.floor(i ** 0.5)
    for j in range(2, sqrt + 1):
        if not i % j:
            count = 0
            while i % j == 0:
                count += 1
                i //= j
            dic[j] += count
    if i > 1:
        dic[i] += 1
values = np.array(list(dic.values()))
v1 = len(values[values >= 2])
v2 = len(values[values >= 4])
v = (v2 * (v2 - 1) // 2) * (v1 - 2)

v3 = len(values[values >= 24])
v += v3 * (v1 - 1)

v4 = len(values[values >= 14])
v += v4 * (v2 - 1)

v5 = len(values[values >= 74])
v += v5
print(v)
