import collections
import numpy as np
n = int(input())
a = list(map(int, input().split()))
counter = collections.Counter(a)
nums = list(counter.values())
num_counter = collections.Counter(nums)
lastest_add = np.count_nonzero(nums)
(building, longests) = ([0], [0])
for i in range(1, n + 1):
    appended = building[-1] + lastest_add
    building.append(appended)
    longests.append(appended // i)
    lastest_add -= num_counter[i]
lastest_longest = 0
k_most = []
for (i, x) in enumerate(reversed(longests)):
    while x > lastest_longest:
        lastest_longest += 1
        k_most.append(n - i)
k_most.extend([0] * (n - len(k_most)))
for longests_num in k_most:
    print(longests_num)
