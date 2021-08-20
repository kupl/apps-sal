import numpy as np
N = int(input())
A = np.array(list(map(int, input().split())), dtype=np.int64)
MOD = 10 ** 9 + 7
B = np.cumsum(A[N - 1:0:-1])[::-1]
B %= MOD
ans = 0
for (i, j) in zip(A[:N - 1], B):
    ans += i * j
    ans %= MOD
print(ans)
