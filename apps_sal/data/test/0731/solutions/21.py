def fhelp(a):
    s = 1
    f = 10
    res = 0
    while a >= s:
        if a >= s and a < f:
            break
        res += len(str(s)) * k * (f - s)
        s *= 10
        f *= 10
    res += len(str(a)) * k * (a - s + 1)
    return res


def f(a, b):
    return fhelp(b) - fhelp(a - 1)


(w, m, k) = list(map(int, input().split()))
l = m - 1
r = 1000000000000000000
while r - l > 1:
    c = (r + l) // 2
    if w >= f(m, c):
        l = c
    else:
        r = c
print(l - m + 1)
