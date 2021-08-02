import numpy as np
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


N = int(readline())
AK = np.array(read().split(), np.int32)

A = AK[::2]; K = AK[1::2]

G = 0

for t in range(50000):
    q = A // K; r = A % K
    q += 1
    r += (-r) % q
    A -= r
    if t % 1000 == 0:
        ind = r != 0
        if np.count_nonzero(~ind):
            G ^= np.bitwise_xor.reduce(A[~ind] // K[~ind])
            A = A[ind]; K = K[ind]
            if len(A) == 0:
                break

answer = 'Takahashi' if G else 'Aoki'
print(answer)
