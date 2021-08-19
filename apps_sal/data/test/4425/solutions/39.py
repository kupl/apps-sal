import math
(N, K) = [int(x) for x in input().split()]
S = 0
for i in range(1, N + 1):
    a = 0
    while i < K:
        a += 1
        i *= 2
    S += 0.5 ** a
ans = S / N
print(ans)
