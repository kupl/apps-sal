import math


def ost(a, b):
    if a % b != 0:
        return 1
    return 0


n, k = map(int, input().split())

ans = 0
for i in range(n):
    f, t = map(int, input().split())
    tmp = 0
    if t > k:
        tmp = f - (t - k)
    else:
        tmp = f
    if i > 0:
        ans = max(tmp, ans)
    else:
        ans = tmp
print(ans)
