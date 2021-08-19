from bisect import bisect_left
from itertools import accumulate


def update(x, delta):
    while x <= n:
        bit[x] += delta
        x += x & -x


def query(x):
    ans = 0
    while x > 0:
        ans += bit[x]
        x -= x & -x
    return ans


(n, t) = list(map(int, input().split()))
arr = list(accumulate(list(map(int, input().split()))))
bit = [0 for i in range(n + 2)]
post = list(sorted([-10 ** 19] + arr))
arr = [0] + arr
leftmost = dict()
for (idx, v) in enumerate(post):
    if v not in leftmost:
        leftmost[v] = idx
res = 0
for i in range(1, len(arr)):
    lower_idx = bisect_left(post, arr[i - 1] + t)
    res += lower_idx - query(lower_idx - 1) - 1
    update(leftmost[arr[i]], 1)
print(res)
