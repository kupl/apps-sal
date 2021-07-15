3

def readln(): return tuple(map(int, input().split()))

cb = cs = cc = 0
for c in list(input()):
    if c == 'B': cb += 1
    if c == 'S': cs += 1
    if c == 'C': cc += 1
nb, ns, nc = readln()
pb, ps, pc = readln()
p, = readln()
a = 0
b = 10**15
while b - a > 1:
    m = (a + b) >> 1
    if max(0, m * cb - nb) * pb + max(0, m * cs - ns) * ps + max(0, m * cc - nc) * pc <= p:
        a = m
    else:
        b = m
print(a)

