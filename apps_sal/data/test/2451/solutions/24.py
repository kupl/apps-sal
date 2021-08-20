(n, h, a, b, k) = list(map(int, input().split()))
for i in range(k):
    (ta, ha, tb, hb) = list(map(int, input().split()))
    m = 0
    if ta != tb:
        if ha < a and hb < a:
            m = a - ha + a - hb + abs(ta - tb)
        elif ha < a and hb >= a:
            m = hb - ha + abs(ta - tb)
        elif ha > b and hb > b:
            m = ha - b + hb - b + abs(ta - tb)
        elif ha > b and hb <= b:
            m = ha - hb + abs(ta - tb)
        else:
            m = abs(ha - hb) + abs(ta - tb)
    else:
        m = abs(ha - hb)
    print(m)
