import math

n = int(input())
ans = 0
for i in range(1, n):
    if not (n - i) % i:
        ans += 1

print(ans)
