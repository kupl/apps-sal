t, w, b = list(map(int, input().split()))


def NOK(a, b):
    m = a*b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a+b)

def NOD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return (a+b)


if w == 1 or b == 1:
    res = t // max (w, b)
else:
    k = NOK(w, b)
    ost = max(0, min(w, b) - 1 - t % k)
    res = (t // k + 1) * min(w,b) - 1 - ost

m = NOD(t, res)

print(str(res // m) + '/' + str(t // m))

