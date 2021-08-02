import numpy as np
N = int(input())
P = [int(i) for i in input().split()]
res = 0
for p, c_min in zip(P, np.minimum.accumulate(P)):
    if p <= c_min: res += 1

print(res)
