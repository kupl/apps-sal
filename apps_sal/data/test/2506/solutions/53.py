from itertools import accumulate
import numpy as np

n, m = list(map(int, input().split()))
A = np.array(input().split(), np.int64)
A = np.sort(A)


def is_ok(x):
    cnt = n**2 - np.searchsorted(A, x - A, side='left').sum()
    if cnt >= m:
        return True
    else:
        return False


l = 0
r = 2 * 10**5 + 1
while l + 1 < r:
    c = (l + r) // 2
    if is_ok(c):
        l = c
    else:
        r = c

B = [0] + list(A)
B = list(accumulate(B))
ans = 0
cnt = 0
for a in A:
    j = np.searchsorted(A, l - a, side='left').sum()
    cnt += n - j
    ans += B[-1] - B[j] + a * (n - j)
ans -= (cnt - m) * l
print(ans)
