def r(): return input()
def ri(): return int(r())
def rr(): return map(int, r().split())
def rl(): return list(rr())


a1, b1 = rr()
a2, b2 = rr()
a3, b3 = rr()


def f(x, y):
    fa = x <= a1 and y <= b1
    fb = x <= b1 and y <= a1
    return fa or fb


f1 = f(max(b2, b3), a2 + a3)
f2 = f(max(a2, a3), b2 + b3)
f3 = f(max(a2, b3), b2 + a3)
f4 = f(max(b2, a3), a2 + b3)

ans = f1 or f2 or f3 or f4
print('YES' if ans else 'NO')
