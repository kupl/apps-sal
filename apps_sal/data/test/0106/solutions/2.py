import sys
import math


def numb(ch):
    pod = ch // (m * k)
    if ch % (m * k) != 0:
        pod += 1
    et = ((ch - 1) % (m * k) + 1) // k
    if ((ch - 1) % (m * k) + 1) % k != 0:
        et += 1
    return(pod, et)


ans = 0
n, m, k = map(int, input().split())
a, b = map(int, input().split())
ans = 0
f_x, f_y = numb(a)
a_x, a_y = numb(b)
if f_x != a_x:
    z = min(math.fabs(f_x - a_x), math.fabs(n - max(f_x, a_x) + min(f_x, a_x)))
    ans += 15 * z
    ans += min(10 + f_y - 1, (f_y - 1) * 5)
    ans += min(10 + a_y - 1, (a_y - 1) * 5)
    print(int(ans))
else:
    ans += min(10 + math.fabs(a_y - f_y), math.fabs(a_y - f_y) * 5)
    print(int(ans))
