from itertools import accumulate
import bisect
n, m, k = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = list(accumulate(A, initial=0))
B = list(accumulate(B, initial=0))
ans = 0
for i, a in enumerate(A):
    remain = k - a
    if remain < 0:
        break
    tmp = i
    tmp += bisect.bisect_right(B, remain) - 1
    ans = max(ans, tmp)
print(ans)
