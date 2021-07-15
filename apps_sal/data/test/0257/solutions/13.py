N,K = map(int,input().split())
XYC = [tuple(map(int,input().split())) for i in range(N)]

from math import hypot,acos,atan2,cos,sin
def circles_cross_points(x1,y1,r1,x2,y2,r2):
    d = hypot(x1-x2, y1-y2)
    if r1 + r2 < d or abs(r1 - r2) >= d: return []
    x = (r1**2 + d**2 - r2**2) / (2*r1*d)
    if not -1 <= x <= 1: return []
    a = acos(x)
    t = atan2(y2-y1, x2-x1)
    return [
        (x1+cos(t+a)*r1, y1+sin(t+a)*r1),
        (x1+cos(t-a)*r1, y1+sin(t-a)*r1)
    ]

eps = 10e-10
def is_ok(t):
    cands = []
    for x,y,_ in XYC:
        cands.append((x,y))
    for i,(x1,y1,c1) in enumerate(XYC[:-1]):
        for x2,y2,c2 in XYC[i+1:]:
            ps = circles_cross_points(x1,y1,t/c1,x2,y2,t/c2)
            cands += ps
    for cx,cy in cands:
        k = 0
        for x,y,c in XYC:
            d = hypot(cx-x,cy-y)
            if c*d <= t + eps:
                k += 1
                if k >= K:
                    return True
    return False

ok = 10**10
ng = 0
for _ in range(100):
    m = (ok+ng)/2
    if is_ok(m):
        ok = m
    else:
        ng = m
    if ok-ng < 10e-7: break
print(ok)
