from math import pi
import sys
sys.setrecursionlimit(10000000)
(n, k) = map(int, input().split())
ans = 0
for i in range(min(n // 2, k)):
    ans += n - 2 * i - 1 + (n - 2 * i - 2)
print(ans)
