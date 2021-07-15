a, b, c = list(map(int, input().split()))
if a % b == 0:
    d = a
else:
    d = (a // b) * b + b  # time
e = (d - a) / 2 + a  # burn
if c % e == 0:
    print((c // e) * d)
else:
    tmp = (c // e) * d
    c -= (c // e) * e
    if c <= a:
        print(tmp + c)
    else:
        c -= a
        print(tmp + a + c * 2)

