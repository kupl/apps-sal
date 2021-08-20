def check(n, t):
    su = t * (t + 1) // 2
    if n >= su:
        return 1
    else:
        return 0


def check2(n, ch, l):
    sua = (ch + l) * (l - ch + 1) // 2
    sub = l * (l - 1) // 2
    if sua + sub > n:
        return 0
    else:
        return 1


(n, h) = list(map(int, input().split()))
l = 0
r = h
while r - l > 1:
    mid = (l + r) // 2
    if check(n, mid):
        l = mid
    else:
        r = mid
ch = 0
if check(n, r):
    ch = r
else:
    ch = l
l = ch
r = 10000000000
while r - l > 1:
    mid = (l + r) // 2
    if check2(n, ch, mid):
        l = mid
    else:
        r = mid
fans = 0
if check2(n, ch, r):
    fans = r
else:
    fans = l
ans = fans + fans - ch
sua = (ch + fans) * (fans - ch + 1) // 2
sub = fans * (fans - 1) // 2
ff = sua + sub
n = n - ff
ans += (n + fans - 1) // fans
print(ans)
