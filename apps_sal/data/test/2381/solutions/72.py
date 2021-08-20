from bisect import bisect_right
(n, k) = list(map(int, input().split()))
A = list(map(int, input().split()))
mod = 10 ** 9 + 7
flag = 0
A.sort()
tmp1 = 1
tmp2 = 1
l = 0
r = n - 1
if k % 2 == 1:
    tmp1 = A[-1] % mod
    r -= 1
    if A[-1] < 0:
        flag = 1
for i in range(k // 2):
    vl = A[l] * A[l + 1]
    vr = A[r] * A[r - 1]
    if max(vl, vr) < 0:
        flag = 1
    if vl > vr:
        l += 2
        tmp1 *= vl
    else:
        r -= 2
        tmp1 *= vr
    tmp1 %= mod
idx = bisect_right(A, 0)
if idx == n:
    idx -= 1
l = max(0, idx - 1)
r = idx
for i in range(k):
    vl = A[l] if l >= 0 else mod
    vr = A[r] if r < n else mod
    if abs(vl) < abs(vr) or r == n:
        l -= 1
        tmp2 *= vl
    else:
        r += 1
        tmp2 *= vr
    tmp2 %= mod
if flag == 0:
    print(tmp1)
else:
    print(tmp2)
