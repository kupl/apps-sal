from bisect import bisect_left, bisect_right
from itertools import accumulate
(n, m) = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()


def isOK(x):
    num = 0
    for (k, a) in enumerate(A, start=1):
        i = bisect_left(A, x - a)
        num += n - i
    return num >= m


l = 0
r = 2 * 10 ** 5 + 1
while l + 1 < r:
    mid = (l + r) // 2
    if isOK(mid):
        l = mid
    else:
        r = mid
s = 0
num = 0
acc = list(accumulate([0] + A))
for a in A:
    i = bisect_right(A, l - a)
    s += a * (n - i) + acc[n] - acc[i]
    num += n - i
ans = s + l * (m - num)
print(ans)
