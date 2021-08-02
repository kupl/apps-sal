# bouncipie
def readint():
    return [int(e) for e in input().split()]


n, m = readint()
x = readint()

sm = [0] * (n + 2)


def addvalue(s, e, v):
    if s > e:
        return
    sm[s] += v
    sm[e + 1] -= v


for (a, b) in zip(x, x[1:]):
    if a == b:
        continue
    if a > b:
        a, b = b, a
    addvalue(1, a - 1, b - a)
    addvalue(a, a, b - 1)
    addvalue(a + 1, b - 1, b - a - 1)
    addvalue(b, b, a)
    addvalue(b + 1, n, b - a)

for i in range(1, n + 2):
    sm[i] += sm[i - 1]

print(' '.join(map(str, sm[1:n + 1])))
