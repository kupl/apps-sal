import numpy as np
N = int(input())
a = list(map(float, input().split()))
a_rev = np.reciprocal(a)
a_rev_sum = np.sum(a_rev)
print(1 / a_rev_sum)
