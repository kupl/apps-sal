import bisect
import math
N, H = map(int, input().split())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
am = max(A)
B.sort()
idx = bisect.bisect_right(B, am)
ans = 0
for i in range(1, N - idx + 1):
    H -= B[-i]
    ans += 1
    if H <= 0:
        print(ans)
        return
print(ans + math.ceil(H / am))
