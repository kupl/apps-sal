import numpy as np
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


N = int(readline())
AK = np.array(read().split(), np.int32)

A = AK[::2]; K = AK[1::2]

for _ in range(50000):
    q = A // K; r = A % K
    q += 1
    r += (-r) % q
    A -= r

A //= K  # grundy
g = np.bitwise_xor.reduce(A)

answer = 'Takahashi' if g else 'Aoki'
print(answer)
