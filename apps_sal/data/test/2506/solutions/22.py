import sys
from itertools import accumulate
from bisect import bisect_left

n, m, *a = list(map(int, sys.stdin.read().split()))
a.sort()


def f(x):
    # 幸福度がx未満となる組み合わせの個数を数える
    cnt = 0
    for ai in a:
        cnt += bisect_left(a, x - ai)
    # 幸福度がx以上の組み合わせの個数がm未満かどうか
    return n * n - cnt < m


left = a[0] * 2
right = a[-1] * 2
while right - left > 1:
    mid = (right + left) // 2
    if f(mid):
        right = mid
    else:
        left = mid
ans = 0
cumsum = [0] + list(accumulate(a))
j = 0
for ai in a:
    i = bisect_left(a, left - ai)
    j += n - i
    ans += ai * (n - i) + cumsum[-1] - cumsum[i]
ans += (m - j) * left
print(ans)
