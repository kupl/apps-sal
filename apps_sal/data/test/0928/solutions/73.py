from bisect import bisect_left
from itertools import accumulate
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a = [0] + list(accumulate(a))


ans = 0
for i in range(n + 1):
    j = bisect_left(a, k + a[i])
    ans = ans + n - j + 1
print(ans)
