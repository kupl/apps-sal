import math
(N, K) = map(int, input().split())
ans = 0
for i in range(1, N + 1):
    if i <= K - 1:
        ans += 1 / N * (1 / 2) ** math.ceil(math.log2(K / i))
    else:
        ans += 1 / N
print(ans)
