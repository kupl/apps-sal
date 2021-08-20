import sys
import math
(a, b, c, d) = list(map(int, sys.stdin.readline().split()))
ans = 1 - (1 - a / b) * (1 - c / d)
ans = 1 / ans
ans = a / b * ans
print(ans)
