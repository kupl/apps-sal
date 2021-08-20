import sys
import math
import random
(n, k) = list(map(int, input().split()))
z = list(map(int, input().split()))
ans = 0
for i in range(n - 1):
    if z[i] + z[i + 1] < k:
        ans += k - z[i + 1] - z[i]
        z[i + 1] += k - z[i + 1] - z[i]
print(ans)
print(*z)
