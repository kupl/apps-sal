def check(v):
    a = v // y - v // (x * y)
    b = v // x - v // (x * y)
    c = v - (a + b + v // (x * y))
    fa = c + a
    fb = min(c, fa - cnt1) + b
    return (fa >= cnt1) and (fb >= cnt2)


cnt1, cnt2, x, y = list(map(int, input().split()))
l, r = 0, (cnt1 + cnt2) * 2
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1
print(ans)
