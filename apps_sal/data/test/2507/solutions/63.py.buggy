import numpy as np

n, k = map(int, input().split())
a = list(map(int, input().split()))
f = list(map(int, input().split()))

if k > sum(a):
    print(0)
    return

a.sort(reverse=True)
f.sort()

a = np.array(a)
f = np.array(f)

lb = -1
ub = a[0] * f[-1]

while ub - lb > 1:
    x = (lb + ub) // 2
    cx = np.full(n, x)
    ck = a - x // f
    ck = np.where(ck < 0, 0, ck)
    ck_sum = ck.sum()
    if ck_sum > k:
        lb = x
    else:
        ub = x
print(ub)
