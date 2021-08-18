import sys
from math import *
n = int(input())
a, b = input(), input()
ans = 0
for i in range(n):
    cur = int(a[i])
    ok = int(b[i])
    cnt1 = 0
    cnt2 = 0
    while cur != ok:
        cur = (cur + 1) % 10
        cnt1 += 1
    cur = int(a[i])
    while cur != ok:
        if cur == 0:
            cur = 9
        else:
            cur -= 1
        cnt2 += 1
    ans += min(cnt1, cnt2)
print(ans)
