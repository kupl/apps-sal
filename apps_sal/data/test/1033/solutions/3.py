n, H = list(map(int, input().split()))
tmp = ((H + 1) * H) >> 1
if n < tmp:
    l, r = 0, 1000000000000000000
    while l < r:
        mid = (l + r) >> 1
        tmp = ((mid + 1) * mid) >> 1
        if n > tmp:
            l = mid + 1
        else:
            r = mid
    print(r)
else:
    l, r = H, 1000000000000000000
    while l < r:
        mid = (l + r) >> 1
        if (mid + H) & 1:
            T = (mid + H) >> 1
            tmp = (((T + H) * (T - H + 1)) >> 1) + ((T * (T + 1)) >> 1)
        else:
            T = (mid + H) >> 1
            tmp = (((T + H) * (T - H + 1)) >> 1) + ((T * (T - 1)) >> 1)
        if n > tmp:
            l = mid + 1
        else:
            r = mid
    print(r)
