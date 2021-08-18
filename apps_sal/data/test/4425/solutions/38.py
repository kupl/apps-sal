from math import log2
import decimal

N, K = map(int, input().split())

decimal.getcontext().prec = 28

ans = decimal.Decimal(0)

for i in range(1, N + 1):
    if i < K:
        power = -(-(log2(K) - log2(i)) // 1)
        prob = decimal.Decimal(1 / ((2**power) * N))
    else:
        prob = decimal.Decimal(1 / N)

    ans = decimal.Decimal(ans + prob)

print(ans)
