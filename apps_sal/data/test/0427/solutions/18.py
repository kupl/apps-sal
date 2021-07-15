cnt1, cnt2, x, y = list(map(int, input().split(' ')))

lo = 1
hi = 10**10

while lo < hi:
    xx = cnt1
    yy = cnt2
    
    mid = (lo + hi) // 2
    intx = mid // x
    inty = mid // y
    intxy = mid // (x*y)
    notxy = mid - intx - inty + intxy
    notx = mid - intx - notxy
    noty = mid - inty - notxy
    
    xx -= notx
    yy -= noty

    
    if max(xx,0) + max(yy,0) > notxy:
        lo = mid + 1
    else:
        hi = mid
print(lo)

