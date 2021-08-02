import numpy as np
from collections import defaultdict

N, K = list(map(int, input().split()))
As = np.array([0] + list(map(int, input().split())))
# Find (i, j) that satisfies "sum(As[i:j]) % K == j - i"
# If 0 < j - i < K then
#sum(As[i:j]) % K == j - i % K
# <-> (sum(As[:j]) - j) % K == (sum(As[:i]) - i) % K

mods = As % K
csum_mods = np.cumsum(mods)
magic_array = (csum_mods - np.arange(0, N + 1)) % K

indices = defaultdict(list)
for i, m in enumerate(magic_array.tolist()):
    indices[m].append(i)

ans = 0
for ls in list(indices.values()):
    j = 1
    for i in range(len(ls)):
        while j < len(ls):
            if ls[j] - ls[i] < K:
                j += 1
            else:
                break
        ans += j - i - 1

print(ans)
