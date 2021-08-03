import sys


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


class Fraction:
    def __init__(self, p=0, q=1, reduced=True):
        if type(p) == int:
            self.p = p
            if type(q) == int:
                self.q = q
        elif type(p) == Fraction:
            self.p = p.p
            self.q = p.q
        else:
            i = p.find(' ')
            if i == -1:
                i = p.find('/')
            if i == -1:
                self.p = int(p)
                self.q = 1
            else:
                self.p = int(p[:i])
                self.q = int(p[i + 1:])
        if reduced:
            self.reduce()

    def reduce(self):
        g = gcd(self.p, self.q)
        self.p //= g
        self.q //= g

    def __str__(self):
        if self.q == 1:
            return(str(self.p))
        else:
            return(str(self.p) + '/' + str(self.q))

    def __lt__(self, other):
        self.reduce()
        if type(other) == float or type(other) == int:
            return self.p < other * self.q
        else:
            other.reduce()
            return self.p * other.q < self.q * other.p

    def __le__(self, other):
        self.reduce()
        if type(other) == float or type(other) == int:
            return self.p <= other * self.q
        else:
            other.reduce()
            return self.p * other.q <= self.q * other.p

    def __gt__(self, other):
        self.reduce()
        if type(other) == float or type(other) == int:
            return self.p > other * self.q
        else:
            other.reduce()
            return self.p * other.q > self.q * other.p

    def __ge__(self, other):
        self.reduce()
        if type(other) == float or type(other) == int:
            return self.p >= other * self.q
        else:
            other.reduce()
            return self.p * other.q >= self.q * other.p

    def __eq__(self, other):
        self.reduce()
        if type(other) == float or type(other) == int:
            return self.p == other * self.q
        else:
            other.reduce()
            return self.p * other.q == self.q * other.p

    def __ne__(self, other):
        self.reduce()
        if type(other) == float or type(other) == int:
            return self.p != other * self.q
        else:
            other.reduce()
            return self.p * other.q != self.q * other.p

    def __mul__(self, other):
        self.reduce()
        if type(other) == int:
            return Fraction(self.p * other, self.q)
        elif type(other) == float:
            return self.p * other / self.q
        else:
            return Fraction(self.p * other.p, self.q * other.q)

    def __rmul__(self, other):
        self.reduce()
        if type(other) == int:
            return Fraction(self.p * other, self.q)
        elif type(other) == float:
            return self.p * other / self.q
        else:
            return Fraction(self.p * other.p, self.q * other.q)

    def __imul__(self, other):
        self = self * other
        return self

    def __truediv__(self, other):
        self.reduce()
        if type(other) == int:
            return Fraction(self.p, self.q * other)
        elif type(other) == float:
            return self.p / self.q / other
        else:
            return Fraction(self.p * other.q, self.q * other.p)

    def __rtruediv__(self, other):
        self.reduce()
        if type(other) == int:
            return Fraction(self.q * other, self.p)
        elif type(other) == float:
            return other * self.q / self.p
        else:
            return Fraction(self.q * other.p, self.p * other.q)

    def __itruediv__(self, other):
        self = self / other
        return self

    def __pow__(self, other):
        if type(other) == int:
            if other >= 0:
                return Fraction(self.p ** other, self.q ** other, False)
            else:
                return Fraction(self.q ** (-other), self.p ** (-other), False)
        elif type(other) == float:
            return (self.p / self.q) ** other
        else:
            return (self.p / self.q) ** (other.p / other.q)

    def __rpow__(self, other):
        if type(other) == int or type(other) == float:
            return other ** (self.p / self.q)
        else:
            return (other.p / other.q) ** (self.p / self.q)

    def __ipow__(self, other):
        self = self ** other
        return self

    def __add__(self, other):
        self.reduce()
        if type(other) == int:
            return Fraction(self.p + self.q * other, self.q)
        elif type(other) == float:
            return self.p / self.q + other
        else:
            return Fraction(self.p * other.q + self.q * other. p, self.q * other.q)

    def __radd__(self, other):
        self.reduce()
        if type(other) == int:
            return Fraction(self.p + self.q * other, self.q)
        elif type(other) == float:
            return self.p / self.q + other
        else:
            return Fraction(self.p * other.q + self.q * other. p, self.q * other.q)

    def __iadd__(self, other):
        self.reduce()
        self = self + other
        return self

    def __sub__(self, other):
        self.reduce()
        if type(other) == int:
            return Fraction(self.p - self.q * other, self.q)
        elif type(other) == float:
            return self.p / self.q - other
        else:
            return Fraction(self.p * other.q - self.q * other. p, self.q * other.q)

    def __rsub__(self, other):
        self.reduce()
        if type(other) == int:
            return Fraction(self.q * other - self.p, self.q)
        elif type(other) == float:
            return other - self.p / self.q
        else:
            return Fraction(self.q * other. p - self.p * other.q, self.q * other.q)

    def __pos__(self):
        return Fraction(+self.p, +self.q)

    def __neg__(self):
        return Fraction(-self.p, self.q)

    def __abs__(self):
        if self.p < 0:
            return -self
        else:
            return self

    def __int__(self):
        return self.p // self.q

    def __float__(self):
        return self.p / self.q

    def __round__(self, digits=0):
        return round(float(self), digits)


a, b, c, d = list(map(int, input().split()))
product = a * c
B1 = b * c
B2 = a * d
if B1 > B2:
    B1, B2 = B2, B1
ans = Fraction(B2 - B1, B2)
ans.reduce()
if ans != 0:
    print(abs(ans))
else:
    print("0/1")
