import bisect
import itertools
n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ca = [0] + list(itertools.accumulate(a))
cb = [0] + list(itertools.accumulate(b))
ans = 0
for i in range(n + 1):
    bk = ca[i]
    if bk <= k:
        j = bisect.bisect(cb, k - bk)
        ans = max(ans, i + j - 1)
    else:
        break
print(ans)
