import numpy as np

n, k = list(map(int, input().split()))
a = np.array(list(map(int, input().split())))

L = len(f'{10**12:b}')
res = 0
for i in range(-1, L):
    if i != -1 and not (k >> i) & 1:
        continue
    val = 0
    for j in range(L):
        d = np.count_nonzero((a >> j) & 1)
        if i < j:
            if (k >> j) & 1:
                val += (n-d) * 2**j
            else:
                val += d * 2**j
        elif i == j:
            val += d * 2**j
        else:
            val += max(d, n-d) * 2**j
    res = max(res, val)
print(res)

