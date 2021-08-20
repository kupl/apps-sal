import copy
import numpy as np
n = int(input())
v = list(map(int, input().split()))
a = v[0::2]
b = v[1::2]
cnta = np.zeros(10 ** 5 + 1, dtype=int)
cntb = np.zeros(10 ** 5 + 1, dtype=int)
for i in range(n // 2):
    (ca, cb) = (a[i], b[i])
    cnta[ca] += 1
    cntb[cb] += 1
la = np.zeros((2, 2), dtype=int)
lb = np.zeros((2, 2), dtype=int)
for i in range(2):
    ia = cnta.argmax()
    ib = cntb.argmax()
    (la[i][0], la[i][1]) = (ia, cnta[ia])
    (lb[i][0], lb[i][1]) = (ib, cntb[ib])
    cnta[ia] = 0
    cntb[ib] = 0
if la[0][0] != lb[0][0]:
    ans = n // 2 - la[0][1] + n // 2 - lb[0][1]
else:
    ans = min(n // 2 - la[0][1] + n // 2 - lb[1][1], n // 2 - la[1][1] + n // 2 - lb[0][1])
print(ans)
