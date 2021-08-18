n, h = map(int, input().split())


def fun(t, h):
    if t <= h:
        return (t * t + t) // 2
    if (t - h) % 2 == 1:
        ret = h + (t - h) // 2
        ans = (t - h) // 2 + 1
        return ans * (h + ret) // 2 + ret * (ret + 1) // 2
    ret = h + (t - h) // 2
    ans = (t - h) // 2 + 1
    return ans * (h + ret) // 2 + ret * (ret - 1) // 2


l = 1
r = 1000000000000000000
while l < r:
    m = (l + r) // 2
    if n > fun(m, h):
        l = m + 1
    else:
        r = m
print(l)
