import numpy as np
from numpy.fft import rfft, irfft
mod = 10 ** 9 + 7
S = input()
mat = []
for i in range(6):
    w = np.zeros(13)
    for j in range(10):
        w[10 ** i * j % 13] += 1
    mat.append(rfft(w))
ress = [[10 ** i * j % 13 for j in range(10)] for i in range(6)]
state = np.zeros(13)
state[0] = 1
state = rfft(state)
keta = 0
res = 5
for s in reversed(S):
    if s == '?':
        state = state * mat[keta % 6]
    else:
        res -= ress[keta % 6][int(s)]
    if state[0] >= 2 ** 50:
        state = np.round(irfft(state, 13))
        state = rfft(np.remainder(state, mod))
    keta += 1
state = irfft(state, 13)
print(int(np.round(np.real(state[res % 13]))) % mod)
