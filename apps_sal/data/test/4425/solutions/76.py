import math
(N, K) = map(int, input().split())
ans = 0
for i in range(1, N + 1):
    if i <= K:
        ans += 1 / N * 0.5 ** math.ceil(math.log2(K / i))
    else:
        ans += 1 / N
print(ans)
