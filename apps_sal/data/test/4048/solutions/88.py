import math
N = int(input())
ans = N - 1
for i in range(1, int(math.sqrt(N)) + 1):
    if N % i == 0:
        ans = min(ans, N // i + i - 2)
print(ans)
