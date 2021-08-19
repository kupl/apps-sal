(l, r, x, y, k) = map(int, input().split())
(low_ex, high_ex) = (x * k, y * k)
if high_ex < l or low_ex > r:
    print('NO')
else:
    low = l // k * k
    up = r // k * k + k
    a = low
    b = low // k
    ok = 0
    while a <= up:
        if x <= b and b <= y and (l <= a) and (a <= r):
            ok = 1
        a += k
        b += 1
    if ok == 1:
        print('YES')
    else:
        print('NO')
