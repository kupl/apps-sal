import math
n = int(input())
ans = n - 1
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        ans = min(ans, i - 1 + n // i - 1)
print(ans)
