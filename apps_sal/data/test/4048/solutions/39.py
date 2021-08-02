import math
n = int(input())

ans = float("inf")
for i in range(1, int(math.sqrt(n) + 1)):
    if n % i == 0:
        if (i - 1) + (n // i - 1) < ans:
            ans = (i - 1) + (n // i - 1)

print(ans)
