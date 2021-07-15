f = lambda: map(int, input().split())
m = 1000000007
n, b, k, x = f()
s = [0] * x
for q in f(): s[q % x] += 1

def g(t, d):
    if not t: return s
    p = [0] * x
    for i, a in enumerate(t):
        for j, b in enumerate(s):
            p[(i + d * j) % x] += a * b
    return [q % m for q in p]

t = []
u, v = 1, 10
while b:
    if b & 1:
        t = g(t, u)
        u = v * u % x
    s = g(s, v)
    v = v * v % x
    b >>= 1
print(t[k])
