from math import gcd
p = 10 ** 9 + 7


class RN:
    p = 10 ** 9 + 7

    def __init__(self, u, d):
        self.u = u
        self.d = d

    def __str__(self):
        return str(self.u) + '/' + str(self.d)

    def cleanup(self):
        self.u = self.u % p
        self.d = self.d % p

    def add(self, u, d):
        self.u = self.u * d + u * self.d
        self.d = self.d * d
        self.cleanup()

    def mult(self, u, d):
        return (self.u * u % p, self.d * d % p)

    def mult_ip(self, u, d):
        (self.u, self.d) = (self.u * u, self.d * d % p)

    def get_m_exp(self):
        self.cleanup()
        a = gcd(self.u, self.d)
        self.u //= a
        self.d //= a
        return pow(self.d, p - 2, p) * self.u % p


(n, m) = tuple(map(int, input().split()))
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))


def sum_ch(n):
    return (n + 1) * n // 2


def sol(s1, s2, m):
    strgr = RN(0, 1)
    eq = RN(1, 1)
    for (gr, sm, i) in zip(s1, s2, list(range(len(s1)))):
        strgr.cleanup()
        if gr != 0 and sm != 0:
            if gr == sm:
                continue
            elif gr < sm:
                return strgr.get_m_exp()
            else:
                strgr.add(eq.u, eq.d)
                return strgr.get_m_exp()
        else:
            if gr == sm == 0:
                strgr.add(*eq.mult(sum_ch(m - 1), m * m))
            elif gr == 0:
                strgr.add(*eq.mult(m - sm, m))
            else:
                strgr.add(*eq.mult(gr - 1, m))
            eq.mult_ip(1, m)
    return strgr.get_m_exp()


'\na = sol([0,0],[1,1], 2) # 3/4\n\na = sol([0,0,0],[1,1,1], 2) # 7/8\na = sol([0,1,1],[1,1,1], 2) # 1/2\na = sol([1,0,1],[1,1,1], 2) # 1/2\n\na = sol([0,0,0],[1,3,3], 3) # 2/2\na = sol([0,0,0],[1,1,0], 2) # 5/8\na = sol([0,0,0],[0,0,0], 2) # 13/16\n'
print(sol(s1, s2, m))
