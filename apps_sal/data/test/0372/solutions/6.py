from math import pi
from decimal import *

getcontext().prec = 100

def cos(x):
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 0, 0, 1, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s


def acos(x):
    mn, mx = Decimal(0), Decimal(pi)
    for i in range(1000):
        md = (mn+mx)/2
        if cos(md) <= x:
            mx = md
        else:
            mn = md
    return mx;


def main():
    x1, y1, r1 = list(map(int, input().split()))
    x2, y2, r2 = list(map(int, input().split()))

    x1, y1, r1 = Decimal(x1), Decimal(y1), Decimal(r1)
    x2, y2, r2 = Decimal(x2), Decimal(y2), Decimal(r2)
    
    
    dcx, dcy = x2-x1, y2-y1
    d = dcx**2 + dcy**2

    if d >= (r1+r2)**2:
        print("0")
        return

    if d <= (r2-r1)**2:
        print("%.7f"%(Decimal(pi)*r1.min(r2)**2))
        return
    
    d = d.sqrt()
    
    ans = r1*r1*acos((d*d+r1*r1-r2*r2)/(2*d*r1)) + r2*r2*acos((d*d+r2*r2-r1*r1)/(2*d*r2))
    ans = ans - Decimal((d + r1 + r2) * (-d + r1 + r2) * (d + r1 - r2) * (d + r2 - r1)).sqrt()/2
    
    print("%.7f"%(ans))

main()

