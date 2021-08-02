from itertools import accumulate
import bisect

n = int(input())
v = list(map(int, input().split()))
t = list(map(int, input().split()))

ns = [0] * n
lo = [0] * n

tt = list(accumulate(t))
# print(tt)
for i in range(n):
    dd = v[i]
    a = 0
    if i != 0:
        dd += tt[i - 1]
        a = tt[i - 1]
    ns[i] += 1
    k = bisect.bisect_right(tt, dd)
    # print(dd,k)
    if k < n:
        ns[k] -= 1

        lo[k] += + v[i] + a
        if k != 0:
            lo[k] -= tt[k - 1]
# print(lo)
ns = list(accumulate(ns))
# print(ns)
for i in range(n):
    lo[i] += t[i] * ns[i]

print(' '.join(list(map(str, lo))))
