import io
import sys
import math
data = input()
n = len(data)
ans = n
for i in range(n - 1):
    if data[i] != data[i + 1]:
        ans = min(ans, max(i + 1, n - i - 1))
print(ans)
