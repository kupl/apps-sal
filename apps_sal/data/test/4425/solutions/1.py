import math

N, K = map(int, input().split())

res = max(0, N - K + 1)

for i in range(1, min(N + 1, K)):
    res += 0.5**math.ceil(math.log2(K / i))

print(res / N)
