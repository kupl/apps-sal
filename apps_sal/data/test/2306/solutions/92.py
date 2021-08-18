
import io
import math
import scipy.sparse
import numpy

data = int(input())

array1 = list(map(lambda x: int(x) * 2, input().split()))

array2 = list(map(lambda x: int(x) * 2, input().split()))

sumt = sum(array1)

maxv = [min(i, sumt - i) for i in range(sumt + 1)]

counter = 0

for t, v in zip(array1, array2):
    for i in range(counter, counter + t + 1):
        maxv[i] = min(maxv[i], v)
    counter += t

for i in range(sumt):
    maxv[i + 1] = min(maxv[i + 1], maxv[i] + 1)
for i in reversed(range(sumt)):
    maxv[i] = min(maxv[i], maxv[i + 1] + 1)

print(sum(maxv) / 4)
