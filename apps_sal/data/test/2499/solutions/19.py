import numpy as np
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
N = int(input())
A = np.array([int(x) for x in input().split()], dtype=np.int64)
'\nF_2 上の線形代数。基本変形で簡単な基底を得る。\n'
xor = np.bitwise_xor.reduce(A)
A = np.concatenate([np.array([1 << i for i in range(60) if xor & 1 << i], np.int64), A])
for k in range(60, -1, -1):
    bit = 1 << k
    one = A & bit != 0
    i = np.where(one & (A < 1 << k + 1))[0]
    if len(i) == 0:
        continue
    i = i[0]
    x = A[i]
    A[one] ^= x
    A[i] = x
A = A[A != 0]
A.sort()
A = A[::-1]
if len(A) > 0:
    red = np.bitwise_xor.reduce(A)
else:
    red = 0
blue = red ^ xor
answer = red + blue
print(answer)
