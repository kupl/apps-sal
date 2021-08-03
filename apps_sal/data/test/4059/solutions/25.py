import math

n = int(input())

ans = 0

for i in range(1, n):
    ans += math.floor((n - 1) / i)

print(ans)
