import math
N, K = map(int, input().split())
ans = 0
for i in range(1, N + 1):
    a = math.log2(K / i)
    if a > 0:
        ans += 0.5**math.ceil(math.log2(K / i)) / N
    else:
        ans += 1 / N
print(ans)
