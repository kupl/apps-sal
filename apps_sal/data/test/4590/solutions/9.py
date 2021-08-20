import itertools
import bisect
(n, m, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ca = [0] + list(itertools.accumulate(a))
cb = [0] + list(itertools.accumulate(b))
ans = 0
for i in range(n + 1):
    if k < ca[i]:
        break
    j = bisect.bisect(cb, k - ca[i])
    ans = max(i - 1 + j, ans)
print(ans)
