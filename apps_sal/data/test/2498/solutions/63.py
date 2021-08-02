import numpy as np
from math import ceil

n, m = map(int, input().split())
a = list(map(int, input().split()))
a = [x // 2 for x in a]
lcm = np.lcm.reduce(a)
ans = 0

for i in a:
    if lcm // i % 2 == 0:
        break
else:
    ans = ceil((m // lcm) / 2)

print(ans)
