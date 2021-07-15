import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

import numpy as np
from numpy.fft import rfft, irfft
import itertools

P = int(input())
A = [int(x) for x in input().split()]

fft_len = 6144
def fft_convolve(A,B):
    C = irfft(rfft(A,fft_len) * rfft(B,fft_len))
    C = (C + .5).astype(np.int64)
    C[:P] += C[P:P+P]
    return C[:P] % P
  
one = np.array([1], dtype=np.int64)
arr = [np.array([(-x)%P,1],dtype=np.int64) for x in range(P)]
L = [one] + list(itertools.accumulate(arr[:-1],lambda a,b: np.convolve(a,b) % P))
R = ([one] + list(itertools.accumulate(arr[1:][::-1],lambda a,b: np.convolve(a,b) % P)))[::-1]
X = [fft_convolve(A,B) % P for A,B in zip(L,R)]

f = np.zeros(P,dtype=np.int64)
for a,x in zip(A,X):
    if a == 1:
        f -= x

f %= P
print((*f))

