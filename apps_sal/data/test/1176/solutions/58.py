import numpy as np

n = int(input())
a = list(map(int, input().split(' ')))

minus_signs = sum([1 for _ in a if np.sign(_) == -1])

if minus_signs % 2 == 0:
    res = sum([abs(_) for _ in a])
else:
    _min = min([abs(_) for _ in a])
    res = sum([abs(_) for _ in a])

    res = res - _min - _min

print(res)
