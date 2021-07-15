import math
n = int(input())
ans = 10 ** 9 + 7
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        ans = min(ans, i + n // i)
    else:
        ans = min(ans, i + n // i + 1)
print(ans)

