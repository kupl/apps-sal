from itertools import accumulate
from math import inf


def sum(p):
    return h[p] - h[ind] + val


def check(p):
    return sum(p) >= el


def binSearch(a, b):
    (left, right) = (a - 1, b + 1)
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid
    return right


(n, q) = list(map(int, input().split()))
a = list(map(int, input().split()))
k = list(map(int, input().split()))
h = [0] + list(accumulate(a)) + [inf]
ind = 1
val = a[0]
ans = list()
for (i, el) in enumerate(k):
    if el < val:
        val -= el
        ans.append(n + 1 - ind)
    elif el == val:
        ind += 1
        if ind == n + 1:
            ind = 1
            val = a[0]
            ans.append(n)
        else:
            val = a[ind - 1]
            ans.append(n + 1 - ind)
    else:
        b = binSearch(ind, n)
        delta = sum(b) - el
        if b == n + 1:
            ans.append(n)
            ind = 1
            val = a[0]
        elif delta == 0:
            ind = b + 1
            if ind == n + 1:
                ind = 1
                val = a[0]
                ans.append(n)
            else:
                val = a[ind - 1]
                ans.append(n + 1 - ind)
        else:
            ind = b
            val = delta
            ans.append(n + 1 - ind)
print('\n'.join(map(str, ans)))
