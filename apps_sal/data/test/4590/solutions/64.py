from itertools import accumulate
from bisect import bisect_right
from sys import stdin


def nii():
    return map(int, stdin.readline().split())


def lnii():
    return list(map(int, stdin.readline().split()))


(n, m, k) = nii()
a = lnii()
b = lnii()
ar = [0] + list(accumulate(a))
br = list(accumulate(b))
ans = 0
for i in range(n + 1):
    time = ar[i]
    if time > k:
        break
    t_ans = i
    inx = bisect_right(br, k - time)
    t_ans += inx
    ans = max(ans, t_ans)
print(ans)
