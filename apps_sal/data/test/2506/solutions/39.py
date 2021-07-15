import numpy as np
from numpy.fft import rfft,irfft
N,M = map(int,input().split())
A = list(map(int,input().split()))
a = np.zeros(10**5+1)
for i in range(N):
    a[A[i]] += 1
b = rfft(a,2*10**5+1)
b = irfft(b*b,2*10**5+1)
b = np.rint(b).astype(np.int64)
c = 0
ans = 0
for n in range(2*10**5,1,-1):
    if c+b[n]<M:
        c += b[n]
        ans += b[n]*n
    else:
        ans += (M-c)*n
        c = M
        break
print(ans)
