import numpy as np

n = int(input())
x = [tuple(map(int, input().split())) for _ in range(n)]

def circle(x, y, z):

    ra = np.array(x)
    rb = np.array(y)
    rc = np.array(z)

    A = np.dot(rb-rc,rb-rc)
    B = np.dot(rc-ra,rc-ra)
    C = np.dot(ra-rb,ra-rb)

    T = A*(B+C-A)
    U = B*(C+A-B)
    W = C*(A+B-C)

    rcc = (T*ra + U*rb + W*rc)/(T + U + W)

    return rcc

def dis(a, b, c, d):
    return (a - b)**2 + (c - d)**2

e = 10 ** (-9)
ans = 10 ** 18
for i in range(n):
    for j in range(i+1, n):
        a = x[i]
        b = x[j]
        px, py = (a[0]+b[0])/2, (a[1]+b[1])/2
        r = dis(px, a[0], py, a[1])
        ok = True
        for s, t in x:
            if dis(px, s, py, t) > r + e:
                ok = False
                break
        if ok:
            ans = min(ans, r)

if ans != 10 ** 18:
    print(ans ** (1/2))
    return

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            a = x[i]
            b = x[j]
            c = x[k]
            px, py = circle(a, b, c)
            r = dis(px, a[0], py, a[1])
            ok = True
            for s, t in x:
                if dis(px, s, py, t) > r + e:
                    ok = False
                    break
            if ok:
                ans = min(ans, r)

print(ans ** (1/2))
