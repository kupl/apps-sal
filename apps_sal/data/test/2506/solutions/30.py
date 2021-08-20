import numpy as np
from numpy.fft import rfft, irfft
(N, M) = list(map(int, input().split()))
(*A,) = list(map(int, input().split()))
B = np.zeros(5 * 10 ** 5)
for a in A:
    B[a] += 1
L = 5 * 10 ** 5
FB = rfft(B, L)
C = np.rint(irfft(FB * FB)).astype(int)
ans = 0
for i in range(2 * 10 ** 5, -1, -1):
    c = C[i]
    if not c:
        continue
    if M - c > 0:
        ans += i * c
        M -= c
    else:
        ans += i * M
        break
print(ans)
