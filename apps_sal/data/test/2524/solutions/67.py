import numpy as np

n=int(input())
a=np.array(list(map(int,input().split())))
mod=10**9+7

s=0
for i in range(60):
    bit = np.count_nonzero(a & 1)
    s += bit*(n-bit)*(2**i)
    a >>= 1
print(s % mod)
