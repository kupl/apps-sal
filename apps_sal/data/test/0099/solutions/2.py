b1, q, l, m = [int(i) for i in input().split()]

a = [int(i) for i in input().split()]

ans = 0

if abs(b1) > l:
    ans = 0
elif b1 == 0:
    ans = "inf" if 0 not in a else 0
else:
    ans = int(b1 not in a)
    if q == 0:
        if 0 not in a : ans = "inf"
    elif q == 1:
        if ans > 0 : ans = "inf"
    elif q == -1:
        if ans > 0 or -b1 not in a: ans = "inf"
    else:
        while 1:
            b1 *= q
            if abs(b1) > l: break
            ans += b1 not in a

print(ans)

