from decimal import Decimal, getcontext
 
class Trigonometry():
    def __init__(self, precision):
        getcontext().prec = precision
        self.pi = self._pi_()
 
    def _pi_(self):
        lo, hi = Decimal('3.14'), Decimal('3.15')
        while True:
            mid = (lo + hi) / 2
            if mid == lo or mid == hi:
                break
            if self.sin(mid) < 0:
                hi = mid
            else:
                lo = mid
        return lo
 
    def sin(self, x):
        res = x
        xpow = x
        fact = Decimal(1)
        k = 3
        while True:
            xpow *= -x * x
            fact *= k * (k - 1)
            next = res + xpow / fact
            if res == next:
                break
            res = next
            k += 2
        return res
 
    def cos(self, x):
        res = Decimal(1)
        xpow = Decimal(1)
        fact = Decimal(1)
        k = 2
        while True:
            xpow *= -x * x
            fact *= k * (k - 1)
            next = res + xpow / fact
            if res == next:
                break
            res = next
            k += 2
        return res
 
    def exp(self, x):
        res = Decimal(1)
        xpow = Decimal(1)
        fact = Decimal(1)
        k = 1
        while True:
            xpow *= x
            fact *= k
            next = res + xpow / fact
            if res == next:
                break
            res = next
            k += 1
        return res
 
    def acos(self, x):
        lo, hi = Decimal(0), self.pi
        while True:
            mid = (lo + hi) / 2
            if mid == lo or mid == hi:
                break
            if self.cos(mid) < x:
                hi = mid
            else:
                lo = mid
        return lo
 
    def asin(self, x):
        lb, ub = -self.pi / 2, self.pi / 2
        while True:
            mid = (lo + hi) / 2
            if mid == lo or mid == hi:
                break
            if self.sin(mid) < x:
                lo = mid
            else:
                hi = mid
        return lo
 
T = Trigonometry(100)
 
x1, y1, r1 = map(Decimal, input().split())
x2, y2, r2 = map(Decimal, input().split())
 
d = ((x1 - x2)**2 + (y1 - y2)**2).sqrt()
 
if r1 + r2 <= d:
    s = 0
 
elif abs(r1 - r2) < d < r1 + r2:
 
    cos_ph1 = (d**2 + r1**2 - r2**2) / (2 * d * r1)
    cos_ph2 = (d**2 + r2**2 - r1**2) / (2 * d * r2)
    ph1 = T.acos(cos_ph1)
    ph2 = T.acos(cos_ph2)
    a = r1**2 * ph1 + r2**2 * ph2
    b = 4 * (d**2) * (r1**2) - (d**2 + r1**2 - r2**2)**2
    s = (4 * (a**2) - b) / (4 * a + 2 * (b.sqrt()))
 
else:
    s = min(r1**2 * T.pi, r2**2 * T.pi)
 
print(s)
