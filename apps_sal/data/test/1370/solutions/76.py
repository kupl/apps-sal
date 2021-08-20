import numpy as np
import itertools
(H, W, K) = map(int, input().split())
choco = []
for i in range(H):
    choco.append([int(x) for x in list(input())])
arr = np.array(choco)
count = H - 1 + (W - 1)
for k in range(H):
    if count <= k:
        break
    for comb in itertools.combinations(range(1, H), k):
        t = (None,) + comb + (None,)
        s = [slice(t[j], t[j + 1]) for j in range(len(t) - 1)]
        sum_p = [0] * (k + 1)
        cut = k
        for col in zip(*choco):
            sum_a = [sum(col[b]) for b in s]
            if any(map(K.__lt__, sum_a)):
                break
            sum_b = [x + y for (x, y) in zip(sum_p, sum_a)]
            if any(map(K.__lt__, sum_b)):
                cut += 1
                sum_p = sum_a
            else:
                sum_p = sum_b
        else:
            count = min(count, cut)
print(count)
