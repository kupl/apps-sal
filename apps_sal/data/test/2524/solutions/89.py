import numpy as np

N = int(input())
A = tuple(map(int, input().split(' ')))
A = np.array(A, dtype=np.int64)
MOD = 10 ** 9 + 7

ans = 0
mask = 1

for i in range(60):
    ones = np.count_nonzero(A & mask)
    ans += (ones * (N - ones) % MOD) * (mask % MOD)
    ans %= MOD
    mask <<= 1

print(ans)
