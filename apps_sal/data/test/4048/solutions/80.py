import math
N = int(input())
ans = 10 ** 12
for i in range(1, int(math.sqrt(N) + 1)):
    if N % i == 0:
        result = i + N // i - 2
        ans = min(ans, result)
print(ans)
