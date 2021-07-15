#!/usr/bin/env python3

def ri():
    return list(map(int, input().split()))

s, x1, x2 = ri()
t1, t2 = ri()
p, d = ri()

if t1 >= t2:
    print(t2*abs(x2-x1))
    return

m = abs(x2-x1)*t2
if d > 0:
    if p <= x1 and x1 <= x2:
        m = min(m, (x2-p)*t1)
    elif p <= x2 and x2 <= x1:
        m = min(m, (s-p+s-x2)*t1)
    elif x1 <= p  and p <= x2:
        m = min(m, (s-p+s+x2)*t1)
    elif x1 <= x2 and x2 <= p:
        m = min(m, (s-p+s+x2)*t1)
    elif x2 <= x1 and x1 <= p:
        m = min(m, (s-p+s-x2)*t1)
    elif x2 <= p and p <= x1:
        m = min(m, (s-p+s-x2)*t1)
else:
    if p <= x1 and x1 <= x2:
        m = min(m, (p+x2)*t1)
    elif p <= x2 and x2 <= x1:
        m = min(m, (p+s+s-x2)*t1)
    elif x1 <= p  and p <= x2:
        m = min(m, (p+x2)*t1)
    elif x1 <= x2 and x2 <= p:
        m = min(m, (p+x2)*t1)
    elif x2 <= x1 and x1 <= p:
        m = min(m, (p-x2)*t1)
    elif x2 <= p and p <= x1:
        m = min(m, (p+s+s-x2)*t1)

print(m)

