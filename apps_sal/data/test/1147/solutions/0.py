import math
import bisect
(n, x, k) = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))
ans = 0
for num in a:
    l = math.ceil(num / x) * x + (k - 1) * x
    r = l + x - 1
    l = num if l < num else l
    ans += bisect.bisect_right(a, r) - bisect.bisect_left(a, l)
print(ans)
'\n7 3 2\n1 3 5 9 11 16 25\n'
'\n4 2 0\n5 3 1 7\n'
