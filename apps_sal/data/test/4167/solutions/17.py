from collections import Counter

import numpy as np

N, K = list(map(int, input().split(' ')))

mods = np.arange(1, N + 1) % K
counter = Counter(mods)

ans = 0
for a in list(counter.keys()):
    if (a + a) % K == 0:
        ans += counter[a] ** 3

print(ans)

