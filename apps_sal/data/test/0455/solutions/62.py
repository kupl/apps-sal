N = int(input())
XY = []
for _ in range(N):
    x, y = list(map(int, input().split()))
    XY.append((x + y, x - y))
if any(XY[0][0] % 2 != xy[0] % 2 for xy in XY):
    print((-1))
    return
odd = XY[0][0] % 2 == 1
if odd:
    d = [2 ** i for i in range(30, -1, -1)]
else:
    d = [2 ** i for i in range(30, -1, -1)] + [1]
print((len(d)))
print((*d))
for xpy, xmy in XY:
    s = ""
    p = 0
    m = 0
    for di in d:
        ps = 1 if p <= xpy else -1
        ms = 1 if m <= xmy else -1
        p += ps * di
        m += ms * di
        if ps == 1:
            s += "R" if ms == 1 else "U"
        else:
            s += "D" if ms == 1 else "L"
    print(s)
