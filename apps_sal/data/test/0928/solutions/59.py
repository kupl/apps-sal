from itertools import accumulate
import bisect
(n, k) = map(int, input().split())
lis = list(map(int, input().split()))
a = [0] + list(accumulate(lis))
ans = 0
for i in a:
    if i < k:
        continue
    ans += bisect.bisect_right(a, i - k)
print(ans)
