from math import log2, ceil
(N, K) = list(map(int, input().split()))
ans = 0
j = 1.0
for x in range(N, 0, -1):
    if x >= K:
        ans += 1.0 * (1 / N)
    else:
        while x * j < K:
            j *= 2.0
        ans += 1.0 / j * (1 / N)
print(ans)
