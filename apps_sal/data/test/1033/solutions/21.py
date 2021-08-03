import math


def cal1(x):
    res = 0
    res = x * (x + 1) // 2
    tot = H + x - 1
    leng = x - H
    res += tot * leng // 2
    return res


def cal2(x):
    res = x * (x + 1) // 2
    return res


a = input().split()
n = int(a[0])
H = int(a[1])
ne = cal1(H)
if n >= ne:
    l = 0
    r = n
    while l < r:
        mid = (l + r + 1) // 2
        if n >= cal1(mid):
            tmp = mid
            l = mid
        else:
            r = mid - 1
    ans = 2 * tmp - H
    if n > cal1(tmp):
        ans += math.ceil((n - cal1(tmp)) / tmp)
else:
    l = 0
    r = n
    while l < r:
        mid = (l + r + 1) // 2
        if n >= cal2(mid):
            tmp = mid
            l = mid
        else:
            r = mid - 1
    ans = tmp
    if n > cal2(tmp):
        ans += math.ceil((n - cal2(tmp)) / tmp)
print(ans)
