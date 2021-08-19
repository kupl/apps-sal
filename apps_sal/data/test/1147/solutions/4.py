import bisect
import math
(n, x, k) = map(int, input().split())
a = sorted(list(map(int, input().split())))
ans = 0
for i in a:
    l = math.ceil(i / x) * x + (k - 1) * x
    r = l + x - 1
    if l < i:
        l = i
    else:
        l = l
    ans += bisect.bisect_right(a, r) - bisect.bisect_left(a, l)
print(ans)
