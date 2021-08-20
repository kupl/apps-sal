import numpy as np
import itertools as itr
N = int(input())
D = list(map(int, input().split()))
tako_cmb = np.array(list(itr.combinations(D, 2)))
xy = tako_cmb.T
result = np.sum(xy[0] * xy[1])
print(result)
