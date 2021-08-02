import numpy as np

n, k = map(int, input().split())
a = np.array(input().split(), np.int64)

a = np.sort(a)
zero = a[a == 0]
pos = a[a > 0]
neg = a[a < 0]


def f(x):
    """count the number of products , <= x"""
    cnt_tpl = 0
    # zero and ...
    if x >= 0:
        cnt_tpl += len(zero) * n
    # positive and ...
    cnt_tpl += np.searchsorted(a, x // pos, side='right').sum()
    # negative and ...
    cnt_tpl += (n - np.searchsorted(a, (-x - 1) // (-neg), side='right')).sum()
    # a^2
    cnt_tpl -= np.count_nonzero(a * a <= x)
    assert cnt_tpl % 2 == 0
    return cnt_tpl // 2


left = -10 ** 18
right = 10 ** 18
while left + 1 < right:
    x = (left + right) // 2
    if f(x) >= k:
        right = x
    else:
        left = x

print(right)
