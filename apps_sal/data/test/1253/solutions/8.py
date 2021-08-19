import sys
import math
(n, k) = [int(x) for x in sys.stdin.readline().split()]
an = [int(x) for x in sys.stdin.readline().split()]
res = 0
j = n
for i in range(n):
    if an[i] < 0:
        if k > 0:
            res += an[i] * -1
            k -= 1
        else:
            res += an[i]
    else:
        j = i
        break
for i in range(j, n):
    res += an[i]
if k > 0:
    if j == n:
        j -= 1
    t = min(int(math.fabs(an[j])), int(math.fabs(an[j - 1])))
    if k % 2 != 0:
        res -= t * 2
print(res)
