import numpy as np
d = [int(x) for x in input().split(" ")]
K = d[1]

d = np.array([int(x) for x in input().split(" ")])

print((np.sort(d)[:K].sum()))


