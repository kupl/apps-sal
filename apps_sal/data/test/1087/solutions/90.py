import numpy as np


def st(n): return bin(n)[2:]


N, K = map(int, input().split())
a = np.array([int(i) for i in input().split()])

MAX = 10**12
mm = MAX.bit_length()
chk = [((a >> K) & 1).sum() for K in range(mm)]

ll = []
q = 0
for num, cc in enumerate(chk):
    if cc < N / 2:
        q += 2**(num)
    ll.append((num, 2**num * (N - cc), 2**num * cc))

max_V = 0
KK = (K + 1).bit_length()
sk = st(K + 1).zfill(mm)
sq = st(q).zfill(mm)

for i in range(KK):
    if (K + 1) >> i & 1 == 1:
        op = q
        if q >> i & 1 == 1:
            op -= 2**i
        I = KK - i
        for j in range(mm - KK + I):
            if sq[j] == '1' and sk[j] == '0':
                op -= 2**(mm - 1 - j)
        V = 0
        for nm, v_1, v_0 in ll:
            if op >> nm & 1 == 1:
                V += v_1
            else:
                V += v_0
        max_V = max(max_V, V)

print(max_V)
