import math
N = int(input())

n = int(math.ceil(math.sqrt(N)))

ans = int(1e18)
for i in range(1, n + 1):
    j = N // i
    if N % i == 0:
        ans = min(ans, j + i - 2)
print(ans)
