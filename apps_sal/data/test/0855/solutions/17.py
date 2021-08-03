def f(): return list(map(int, input().split()))
def g(): return [[0] * 4] + [[0] + f() for i in range(3)]
def h(x, y): return x - 1 == y % 3
def t(a, b, u, v): return (A[a][b], B[a][b], u + h(a, b), v + h(b, a))


k, a, b = f()
p = 2520
s, d = k // p, k % p
if s:
    s, d = s - 1, d + p
A, B = g(), g()
u = v = x = y = 0
for j in range(d):
    a, b, u, v = t(a, b, u, v)
for i in range(p):
    a, b, x, y = t(a, b, x, y)
print(u + x * s, v + y * s)
