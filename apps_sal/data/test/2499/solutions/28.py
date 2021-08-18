import numpy as np
N = int(input())
A = np.array(list(map(int, input().split())), dtype=np.int64)

xor = np.bitwise_xor.reduce(A)

odd_digit = [1 << i for i in range(60) if xor & (1 << i)]

for i in odd_digit:
    A = A & (~i)

for i in range(60, - 1, - 1):
    one_digit = (A & (1 << i) != 0)
    pivot_flag = np.where(one_digit & (A < (1 << (i + 1))))[0]
    if len(pivot_flag) == 0:
        continue
    p = pivot_flag[0]
    pivot = A[p]
    A[one_digit] ^= pivot
    A[p] = pivot

res = sum(odd_digit) + 2 * (np.bitwise_xor.reduce(A))
print(res)
