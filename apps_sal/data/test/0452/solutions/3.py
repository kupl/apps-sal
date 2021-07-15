from fractions import*
from sys import*
from copy import*
from time import*


class Fraction:
    def __init__(self, x = 0, y = 1):
        if(type(x) == str):
            if x.find('/') != -1:
                a = list(map(int, x.split('/')))
            else:
                a = list(map(int, x.split()))
            self.num = a[0]
            if len(a) == 1:
                self.den = 1
            else:
                self.den = a[1]
        elif(type(x) == Fraction):
            self.num, self.den = x.num, x.den
        else:
            self.num, self.den = x, y
        self.reduce()

    def __str__(self):
        if self.den == 1:
            return str(int(self.num))
        return str(int(self.num)) + '/' + str(int(self.den))

    def reduce(self):
        d = gcd(abs(self.num), abs(self.den))
        if self.den < 0:
            self.den, self.num = -self.den, -self.num
        self.num, self.den = self.num // d, self.den // d

    def __lt__(self, other):
        if type(other) == Fraction:
            return self.num * other.den < other.num * self.den
        else:
            return self.num < self.den * other

    def __le__(self, other):
        if type(other) == Fraction:
            return self.num * other.den <= other.num * self.den
        else:
            return self.num <= self.den * other

    def __gt__(self, other):
        if type(other) == Fraction:
            return self.num * other.den > other.num * self.den
        else:
            return self.num > self.den * other

    def __ge__(self, other):
        if type(other) == Fraction:
            return self.num * other.den >= other.num * self.den
        else:
            return self.num >= self.den * other

    def __eq__(self, other):
        if type(other) == Fraction:
            return self.num * other.den == other.num * self.den
        else:
            return self.num == self.den * other

    def __ne__(self, other):
        if type(other) == Fraction:
            return self.num * other.den != other.num * self.den
        else:
            return self.num != self.den * other

    def __mul__(self, other):
        if(type(other) == float):
            return (self.num * other) / self.den
        elif type(other) == Poly:
            return NotImplemented
        else:
            other = Fraction(other)
            return Fraction(self.num * other.num, self.den * other.den)

    def rmul(self, other):
        return other * self

    def __rmul__(self, other):
        if(type(other) == float):
            return (self.num * other) / self.den
        else:
            other = Fraction(other)
            return Fraction(self.num * other.num, self.den * other.den)

    def __imul__(self, other):
        if(type(other) == float):
            self = (self.num * other) / self.den
        else:
            other = Fraction(other)
            self.num *= other.num
            self.den *= other.den
            self.reduce()
        return self

    def __truediv__(self, other):
        if(type(other) == float):
            return self.num / (self.den * other)
        else:
            other = Fraction(other)
            return self * Fraction(other.den, other.num)

    def __rtruediv__(self, other):
        if(type(self) == float):
            return other.num / (other.den * self)
        else:
            self = Fraction(self)
            return other * Fraction(self.den, self.num)

    def __itruediv__(self, other):
        if(type(other) == float):
            self = self.num / (self.den * other)
        else:
            other = Fraction(other)
            self = self * Fraction(other.den, other.num)
            self.reduce()
        return self

    def __pow__(self, other):
        if type(other) == Fraction:
            return (self.num / self.den) ** (other.num / other.den)
        elif type(other) == int:
            if other > 0:
                return Fraction(self.num ** other, self.den ** other)
            else:
                return 1 / Fraction(self.num ** (-other), self.den ** (-other))
        else:
            return (self.num / self.den) ** other

    def __rpow__(self, other):
        return other ** (self.num / self.den)

    def __ipow__(self, other):
        if other > 0:
            self.num **= other
            self.den **= other
        else:
            self.num **= (-other)
            self.den **= (-other)
            self.num, self.den = self.den, self.num
        return self

    def __add__(self, other):
        if type(other) == float:
            return self.num / self.den + other
        elif type(other) == Poly:
            return NotImplemented
        else:
            other = Fraction(other)
            return Fraction(self.num * other.den + other.num * self.den, self.den * other.den)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        if type(other) == float:
            self = self.num / self.den + other
        else:
            other = Fraction(other)
            self.num = self.num * other.den + other.num * self.den
            self.den = self.den * other.den
            self.reduce()
        return self

    def __sub__(self, other):
        if type(other) == float:
            return self.num / self.den - other
        elif type(other) == Poly:
            return NotImplemented
        else:
            other = Fraction(other)
            return Fraction(self.num * other.den - other.num * self.den, self.den * other.den)

    def __rsub__(self, other):
        if(type(self - other) == Fraction):
            return Fraction(-(self - other).num, (self - other).den)
        else:
            return -(self - other)

    def __isub__(self, other):
        if type(other) == float:
            self = self.num / self.den - other
        else:
            other = Fraction(other)
            self.num = self.num * other.den - other.num * self.den
            self.den = self.den * other.den
            self.reduce()
        return self

    def __pos__(self):
        return self

    def __neg__(self):
        return Fraction(-self.num, self.den)

    def __abs__(self):
        return Fraction((-self.num) * int(self.num < 0) + (self.num) * (self.num >= 0), self.den)

    def __int__(self):
        return self.num // self.den

    def __float__(self):
        return self.num / self.den

    def __round__(self, x = 0):
        return round(float(self), x)


class Poly:
    def __init__(self, s = 0):
        if type(s) in [int, float, Fraction]:
            self.list = [s]
        elif type(s) == str:
            self.list, s = [], s.split()
            for elem in S:
                self.list += eval(elem)
        elif type(s) == Poly:
            self.list = s.list
        else:
            self.list = list(s)

    def __str__(self):
        P, S, power, first = [chr(8304), chr(185), chr(178), chr(179)] + [chr(i) for i in range(8308, 8314)], "", len(self.list) - 1, True
        for i in range(len(self.list) - 1, -1, -1):
            current = self.list[i]
            if current != 0:
                if current > 0:
                    S += " + " * int(not first)
                else:
                    S += " - " * int(not first) + "-" * int(first)
                current = abs(current)
                if current != 1 or (current == 1 and power == 0):
                    if type(current) == Fraction:
                        if current.den == 1:
                            S += str(int(current.num))
                        else:
                            S += "(" + str(current) + ")"
                    elif type(current) == float:
                        S += str(round(current, 3))
                    else:
                        S += str(current)
                S += ('x' * (power != 0))
                for elem in str(power):
                    S += P[int(elem)] * (not(elem in ["0", "1"] and len(str(power)) == 1))
                first = len(S) == 0
            power -= 1
        if S == "":
            return "0"
        return S

    def __neg__(self):
        result = []
        for elem in self.list:
            result.append(-elem)
        return Poly(result)

    def __add__(self, other):
        result = []
        if type(other) == Poly:
            for i in range(max(len(self.list), len(other.list))):
                if i < len(self.list):
                    if i < len(other.list):
                        result.append(self.list[i] + other.list[i])
                    else:
                        result.append(self.list[i])
                else:
                    if i < len(other.list):
                        result.append(other.list[i])
                    else:
                        result.append(0)
            return Poly(result)
        else:
            lolka = [self.list[0] + other] + self.list[1:]
            return Poly(lolka)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.list = (self + other).list
        return self

    def __sub__(self, other):
        result = []
        if type(other) == Poly:
            for i in range(max(len(self.list), len(other.list))):
                if i < len(self.list):
                    if i < len(other.list):
                        result.append(self.list[i] - other.list[i])
                    else:
                        result.append(self.list[i])
                else:
                    if i < len(other.list):
                        result.append(-other.list[i])
                    else:
                        result.append(0)
            return Poly(result)
        else:
            lolka = [self.list[0] - other] + self.list[1:]
            return Poly(lolka)

    def __rsub__(self, other):
        return -(self - other)

    def __isub__(self, other):
        self.list = (self - other).list
        return self

    def __or__(self, other):
        if len(self.list) == 1:
            return self.list[0]
        result = self.list[len(self.list) - 1]
        for i in range(len(self.list) - 2, -1, -1):
            result = result * other + self.list[i]
        return result

    def __mul__(self, other):
        result, p = [], Poly(other)
        for i in range(len(self.list)):
            for j in range(len(p.list)):
                if len(result) > i + j:
                    result[i + j] += self.list[i] * p.list[j]
                else:
                    result += [0] * (i + j - len(result)) + [self.list[i] * p.list[j]]
        return Poly(result)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self.list = (self * other).list
        return self

    def __pow__(self, other):
        if other == 0:
            return Poly(1)
        if other % 2 == 1:
            return Poly((self ** (other - 1)) * self)
        else:
            lolka = self ** (other // 2)
            return Poly(lolka * lolka)

    def __ipow__(self, other):
        self.list = (self ** other).list
        return self

    def __divmod__(self, other):
        result = [0] * 100
        p = deepcopy(self.list)
        q = Poly(other).list
        power1, power2 = len(p) - 1, len(q) - 1
        while(power1 > -1 and p[power1] == 0):
            power1 -= 1
        while(power2 > -1 and q[power2] == 0):
            power2 -= 1
        while(power1 > -1 and power2 > -1 and power1 >= power2):
            minus = [0] * (power1 - power2)
            if type(p[power1]) == int and type(q[power2]) == int:
                if p[power1] % q[power2] == 0:
                    current = p[power1] // q[power2]
                else:
                    current = Fraction(p[power1], q[power2])
            else:
                current = p[power1] / q[power2]
            for elem in q:
                minus += [elem * current]
            for i in range(max(len(p), len(minus))):
                if i < len(p):
                    if i < len(minus):
                        p[i] -= minus[i]
                else:
                    if i < len(minus):
                        p.append(-minus[i])
                    else:
                        p.append(0)
            result[power1 - power2] = current
            while(power1 > -1 and p[power1] == 0):
                power1 -= 1
            while(power2 > -1 and q[power2] == 0):
                power2 -= 1
            #result += [current]
        return (Poly(result), Poly(p))

    def __rdivmod__(self, other):
        return  divmod(Poly(other), self)

    def __floordiv__(self, other):
        return divmod(self, other)[0]

    def __rfloordiv__(self, other):
        return divmod(Poly(other), self)[0]

    def __ifloordiv__(self, other):
        self.list = (divmod(self, other)[0]).list
        return self

    def __mod__(self, other):
        return divmod(self, other)[1]

    def __rmod__(self, other):
        return divmod(Poly(other), self)[1]

    def __imod__(self, other):
        self.list = (divmod(self, other)[1]).list
        return self

#begin = time()
p, q = list(map(int, input().split()))
lolka = Fraction(p, q)
n = int(input())
A = list(map(int, input().split()))
Answer = Fraction(A[-1])
for i in range(len(A) - 2, -1, -1):
    Answer = 1 / Answer
    Answer += A[i]
if(Answer == lolka):
    print("YES")
else:
    print("NO")
#print(time() - begin)


