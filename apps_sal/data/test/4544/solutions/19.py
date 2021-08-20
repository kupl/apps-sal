import numpy as np
N = int(input())
A = np.array(input().split(), dtype=np.int32)
counter = np.bincount(A)
if len(counter) <= 2:
    answer = counter.sum()
else:
    answer = (counter[2:] + counter[1:-1] + counter[:-2]).max()
print(answer)
