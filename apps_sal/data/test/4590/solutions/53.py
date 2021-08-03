import itertools
import bisect
n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ca = [0] + list(itertools.accumulate(a))
cb = [0] + list(itertools.accumulate(b))
ans = 0
for i in range(n + 1):
    wk = ca[i]
    if wk > k:
        break
    else:
        j = bisect.bisect(cb, k - ca[i])
        ans = max(ans, i + j - 1)
print(ans)
