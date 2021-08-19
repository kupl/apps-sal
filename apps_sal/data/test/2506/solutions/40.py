import numpy as np
(N, M) = list(map(int, input().split()))
A = np.array(input().split(), dtype=np.int32)
x = np.bincount(A)
fft_size = 1 << (2 * x.size + 10).bit_length()
fx = np.fft.rfft(x, fft_size)
conv = np.fft.irfft(fx * fx, fft_size)
conv = (conv + 0.5).astype(int)
tmp = np.arange(conv.size, dtype=int)
happy = tmp[np.nonzero(conv)].tolist()
cnt = conv[np.nonzero(conv)].tolist()
ans = 0
while M > 0:
    h = happy.pop()
    num = cnt.pop()
    num = min(M, num)
    M -= num
    ans += num * h
print(ans)
