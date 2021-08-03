n = int(input())
wcnt = 0
bcnt = 0
for i in range(n):
    a, b = input().split()
    if b == "soft":
        bcnt = bcnt + 1
    else:
        wcnt = wcnt + 1

if wcnt > bcnt:
    t = wcnt
    wcnt = bcnt
    bcnt = t

lo = 1
hi = 100
while lo < hi:
    mid = (lo + hi) // 2
    if mid * mid // 2 < wcnt or mid * mid - mid * mid // 2 < bcnt:
        lo = mid + 1
    else:
        hi = mid
print(lo)
