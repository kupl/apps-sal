import sys

MOD = 10 ** 9 + 7
INF = 10 ** 9
PI = 3.14159265358979323846


def read_str(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline().strip())
def read_ints(): return map(int, sys.stdin.readline().strip().split())
def read_ints2(x): return map(lambda num: int(num) - x, sys.stdin.readline().strip().split())
def read_str_list(): return list(sys.stdin.readline().strip().split())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))
def GCD(a: int, b: int) -> int: return b if a % b == 0 else GCD(b, a % b)
def LCM(a: int, b: int) -> int: return (a * b) // GCD(a, b)


class Combination():
    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.note = [1, 1]
        self.noteinv = [1, 1]
        self.inv = [0, 1]
        self.calc()

    def calc(self):
        for i in range(2, self.n + 1):
            self.note.append((self.note[-1] * i) % self.p)
            self.inv.append((-self.inv[self.p % i] * (self.p // i)) % self.p)
            self.noteinv.append((self.noteinv[-1] * self.inv[-1]) % self.p)

    def nCr(self, n, r):
        n = self.n
        if r < 0 or n < r:
            return 0
        r = min(r, n - r)
        return (self.note[n] * self.noteinv[r] * self.noteinv[n - r]) % self.p


def Main():
    x, y = read_ints()
    if (x + y) % 3 != 0:
        print(0)
        return
    n = (2 * x - y) // 3
    m = (2 * y - x) // 3
    cmb = Combination(n + m, MOD)
    print(cmb.nCr(n + m, min(n, m)))


def __starting_point():
    Main()


__starting_point()
