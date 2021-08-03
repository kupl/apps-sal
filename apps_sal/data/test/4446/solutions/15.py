import math
import sys
input = sys.stdin.readline
N, a, b, k = list(map(int, input().split()))
h = list(map(int, input().split()))

ans = 0
tmp = []
for i in range(N):
    j = h[i] % (a + b)
    if j > 0 and j <= a:
        ans += 1
    else:
        if j == 0:
            j += b
        else:
            j -= a
        tmp.append(j)

tmp.sort()
for x in tmp:
    if k >= math.ceil(x / a):
        k -= math.ceil(x / a)
        ans += 1
    else:
        break
print(ans)
