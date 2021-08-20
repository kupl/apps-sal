import sys
import numpy as np
import math
n = int(input())
aList = list(map(int, input().split()))
gcdListLeft = [0 for i in range(n)]
gcdListRight = [0 for i in range(n)]
tmp = aList[0]
for i in range(n):
    tmp = gcdListLeft[i] = math.gcd(tmp, aList[i])
tmp = aList[n - 1]
for i in range(n - 1, -1, -1):
    tmp = gcdListRight[i] = math.gcd(tmp, aList[i])
ans = gcdListRight[1]
for i in range(1, n - 1):
    ans = max(ans, math.gcd(gcdListLeft[i - 1], gcdListRight[i + 1]))
ans = max(ans, gcdListLeft[n - 2])
print(ans)
