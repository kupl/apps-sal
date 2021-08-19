import numpy as np
import sys
input = sys.stdin.readline
MOD = 10 ** 9 + 7
(N, K) = map(int, input().split())
U = int(10 ** 4.5 + 10)
div = np.arange(1, U, dtype=np.int64)
div = div[N % div == 0]
div = sorted(np.union1d(div, N // div))
A = {d: pow(K, int((d + 1) // 2), MOD) for d in div}
B = {}
for d in div:
    B[d] = A[d] - sum((B[dd] for dd in div if dd < d and d % dd == 0))
answer = sum((B[d] * (d // 2 if d % 2 == 0 else d) for d in div))
answer %= MOD
print(answer)
