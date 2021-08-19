3
__metaclass__ = type
__author__ = 'xdlove'
(n, k) = list(map(int, input().split()))
res = [int(x) for x in input().split()]
(l, r) = (-1, -2)
(L, num_0) = (0, 0)
for R in range(n):
    if res[R] == 0:
        num_0 += 1
    while num_0 > k:
        if r - l < R - L:
            (l, r) = (L, R)
        if res[L] == 0:
            num_0 -= 1
        L += 1
    if R == n - 1 and r - l < R + 1 - L:
        (l, r) = (L, R + 1)
print(r - l)
for i in range(n):
    if l <= i < r:
        res[i] = 1
    res[i] = str(res[i])
print(' '.join(res))
