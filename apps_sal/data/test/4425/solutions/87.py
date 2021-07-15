import math

N, K = list(map(int, input().split()))

ans = 0
for n in range(1, N+1):
    if n >= K:
        ans += 1/N
        continue
    x = math.ceil(math.log2(K/n))
    ans += (0.5**x)/N

print(ans)

