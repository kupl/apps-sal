# 55:33
import numpy as np

N, K, *XY = list(map(int, open(0).read().split()))

X = XY[::2]
comp_X = {}
decomp_X = {}
for i, x in enumerate(sorted(set(X))):
    comp_X[x] = i
    decomp_X[i] = x

Y = XY[1::2]
comp_Y = {}
decomp_Y = {}
for i, y in enumerate(sorted(set(Y))):
    comp_Y[y] = i
    decomp_Y[i] = y

I = len(comp_X)
J = len(comp_Y)
comp_XY = [(comp_X[x], comp_Y[y]) for x, y in zip(X, Y)]
acc = np.zeros((I + 1, J + 1), np.int32)
for c_x, c_y in comp_XY:
    acc[c_x + 1][c_y + 1] += 1
acc = np.add.accumulate(acc, axis=0)
acc = np.add.accumulate(acc, axis=1)

ans = float("inf")
for i in range(1, I + 1):
    for j in range(1, J + 1):
        cur = acc[i:, j:] + acc[:-i, :-j] - acc[:-i, j:] - acc[i:, :-j]
        for k, row in enumerate(cur):
            for l, val in enumerate(row):
                if val >= K:
                    ans = min(
                        ans,
                        (decomp_X[k + i - 1] - decomp_X[k]) *
                        (decomp_Y[l + j - 1] - decomp_Y[l]),
                    )
print(ans)
