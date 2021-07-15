from sys import stdin
import numpy as np
n, k = list(map(int, stdin.readline().split()))
a = np.array(stdin.readline().split(), dtype=np.int64)

ng = 0
ok = 10 ** 9 + 1
while ok - ng > 1:
    mid = (ok + ng) >> 1
    if np.sum(0 - - a // mid - 1) <= k:
        ok = mid
    else:
        ng = mid
print(ok)

