
"""

created by shuangquan.huang at 11/21/18


Fenwick Tree

prefix sum in s
j < i, s[i]-s[j] < t,

i+1 - (c = count of j that makes s[i]-s[j] >= t)
c = count of s[j] <= s[i] - t


"""
import bisect


N, T = list(map(int, input().split()))

A = [int(x) for x in input().split()]


prefsums = [0] * (N + 1)
for i in range(N):
    prefsums[i + 1] = A[i] + prefsums[i]


MAXNN = len(prefsums) + 1
L = [0] * MAXNN


def lsb(i):
    return i & (-i)


def update(i):
    while i < MAXNN:
        L[i] += 1
        i |= i + 1


def get(i):
    ans = 0
    while i >= 0:
        ans += L[i]
        i = (i & (i + 1)) - 1

    return ans


prefsums = list(sorted(set(prefsums)))
ans = 0
update(bisect.bisect_left(prefsums, 0))

pr = 0
for i, v in enumerate(A):
    pr += v
    npos = bisect.bisect_right(prefsums, pr - T)
    ans += i + 1 - get(npos - 1)
    k = bisect.bisect_left(prefsums, pr)
    update(k)

print(ans)
