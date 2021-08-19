from itertools import accumulate as ac
N = int(input())
A = list(ac(list(map(int, input().split()))))
(l, r, t) = (0, 2, A[-1])
c = t
for m in A[1:-2]:
    while t + m > A[r] + A[r + 1]:
        r += 1
    while m > A[l] + A[l + 1]:
        l += 1
    x = sorted([A[l], m - A[l], A[r] - m, t - A[r]])
    c = min(c, x[-1] - x[0])
print(c)
