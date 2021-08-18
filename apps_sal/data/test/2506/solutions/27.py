import sys
import numpy as np


def convolve(A, B):
    dtype = np.int64
    fft, ifft = np.fft.rfft, np.fft.irfft
    a, b = len(A), len(B)
    if a == b == 1:
        return np.array([A[0] * B[0]])
    n = a + b - 1
    k = 1 << (n - 1).bit_length()
    AB = np.zeros((2, k), dtype=dtype)
    AB[0, :a] = A
    AB[1, :b] = B
    return np.rint(ifft(fft(AB[0]) * fft(AB[1]))).astype(np.int64)[:n]


input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))

cnt = np.zeros(100001)
for i in a:
    cnt[i] += 1

c = convolve(cnt, cnt)
ans = 0
for i in range(len(c))[::-1]:
    if c[i] > 0:
        p = min(m, c[i])
        m -= p
        ans += i * p
        if m == 0:
            break
print(ans)
