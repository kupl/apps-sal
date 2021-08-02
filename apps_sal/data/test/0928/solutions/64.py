import bisect
from itertools import accumulate
n, k = map(int, input().split())
a = [0] + list(accumulate(list(map(int, input().split()))))
ans = 0
for i in range(n):
    ans += n + 1 - bisect.bisect_left(a, k + a[i])
print(ans)
