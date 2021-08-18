import math
from collections import deque
n, k = map(int, input().split())
v = list(map(int, input().split()))
ans = 0
for i in range(1, min(k, n) + 1):
    for m in range(i + 1):
        s = v[:m] + v[n - (i - m):]
        s.sort()
        for j in range(i, min(k, 2 * i)):
            if s[j - i] < 0:
                s[j - i] = 0
        ans = max(ans, sum(s))
print(ans)
