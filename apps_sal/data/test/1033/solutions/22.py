n, H = input().split()

n = int(n)
H = int(H)


def can(m):
    nonlocal n, H
    ans = 0
    tt = min(m, H)
    ans += ((tt + 1) * tt) // 2
    ans += (m - tt) * H
    ost = m - tt
    if ost % 2 == 0:
        up = ost // 2 - 1

        ans += ((up + 1) * up)
        ans += up + 1
    else:
        up = ost // 2
        ans += ((up + 1) * up)
    return ans


l = 0
r = n + H

while r - l > 1:
    m = (l + r) // 2

    if can(m) < n:
        l = m
    else:
        r = m

print(r)
