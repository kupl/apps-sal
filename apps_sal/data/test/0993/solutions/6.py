import numpy as np
from collections import Counter

n, m = map(int, input().split())

a = np.array([0] + list(map(int, input().split())), dtype=np.int64)
a = np.mod(a.cumsum(), m)

c = Counter(a)

ans = 0

for i in c.values():
    ans += i * (i - 1) // 2

print(ans)
