x = int(input())
(hh, mm) = [int(v) for v in input().split()]
ans = 0
while '7' not in '%s%s' % (hh, mm):
    ans += 1
    if x == 60:
        hh -= 1
    else:
        mm -= x
        if mm < 0:
            mm += 60
            hh -= 1
            if hh < 0:
                hh = 23
print(ans)
