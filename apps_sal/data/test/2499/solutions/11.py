import numpy as np

N = int(input())
A = np.array(input().split(),dtype=np.int64)

xor = np.bitwise_xor.reduce(A)
A = np.concatenate([np.array([1<<i for i in range(60) if xor&(1<<i)],np.int64),A])

for k in range(60,-1,-1):
    bit = 1<<k
    one = (A&bit != 0)
    i = np.where(one & (A < (1<<(k+1))))[0]
    if len(i) == 0:
        continue
    i = i[0]
    x = A[i]
    A[one] ^= x
    A[i] = x

red = np.bitwise_xor.reduce(A)
blue = red^xor
answer = red + blue
print(answer)

