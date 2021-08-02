# IAWT
S = input()
a = S[:3]
b = S[3:]


def Sum(st):
    n = 0
    for x in st:
        n += int(x)
    return n


def g(s, t):  # s < t
    diff = int(t[0]) + int(t[1]) + int(t[2]) - int(s[0]) - int(s[1]) - int(s[2])
    ma = 9 - int(s[0])
    c = 0
    if 9 - int(s[1]) > ma:
        c = 1
        ma = 9 - int(s[c])
    if 9 - int(s[2]) > ma:
        c = 2
        ma = 9 - int(s[c])

    mm = int(t[0])
    c2 = 0
    if int(t[1]) > mm:
        mm = int(t[1])
        c2 = 1
    if int(t[2]) > mm:
        mm = int(t[2])

        c2 = 2
    if ma > mm:
        C = str(int(s[c]) + min(diff, ma))
        s = s[:c] + C + s[c + 1:]
    else:
        C = str(int(t[c2]) - min(diff, mm))
        t = t[:c2] + C + t[c2 + 1:]
    return s, t


def f():
    nonlocal a, b
    if Sum(a) == Sum(b):
        print(0)
        return
    if Sum(a) < Sum(b):
        n = 0
        while (Sum(a) != Sum(b)):
            a, b = g(a, b)
            n += 1
        print(n)
        return
    n = 0
    while (Sum(a) != Sum(b)):
        b, a = g(b, a)
        n += 1
    print(n)


f()
