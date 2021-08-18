import bisect
import sys
import math
sys.setrecursionlimit(10**6)


n, h = list(map(int, input().split()))

a = []
b = []
ab = []
for i in range(n):
    a_tmp, b_tmp = list(map(int, input().split()))
    a.append(a_tmp)
    b.append(b_tmp)

a_max = max(a)
b.sort()

index = bisect.bisect_right(b, a_max)

ans = 0
for i in reversed(list(range(index, n))):
    h -= b[i]
    ans += 1
    if h <= 0:
        break

if h > 0:
    ans += math.ceil(h / a_max)

print(ans)
