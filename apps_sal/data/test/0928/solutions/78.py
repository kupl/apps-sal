from itertools import accumulate
from bisect import bisect_left, bisect, bisect_right

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

aa = [0] + list(accumulate(a))

icnt = 0
for i in range(n):
    if aa[i] + k > aa[n]:
        continue
    ii = bisect_left(aa, aa[i] + k)
    icnt += max(n + 1 - ii, 0)

print(icnt)
