import numpy as np
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
MAXBITS = 40
bits = np.ndarray((N, MAXBITS), dtype=int)
for i in range(N):
    a = A[i]
    bits[i] = np.array([(a >> j) & 1 for j in range(MAXBITS - 1, -1, -1)])
sm = bits[0]
for b in bits[1:]:
    sm += b
lower = False
Kbits = np.array([(K >> j) & 1 for j in range(MAXBITS - 1, -1, -1)])
ans = 0
for i in range(MAXBITS):
    ones = sm[i]
    zeros = N - sm[i]
    base = 2**(MAXBITS - i - 1)
    bit = 0
    if ones >= zeros:
        bit = 0
    elif lower or Kbits[i] == 1:
        bit = 1
    if Kbits[i] > bit:
        lower = True
    ans += ones * base if bit == 0 else zeros * base
print(ans)
