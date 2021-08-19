n = int(input())

x = []
y = []

lineas = set()
lineas1 = set()
lineas2 = set()

caca = dict()


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
    for j in range(i):
        a1 = a - x[j]
        b1 = b - y[j]

        p1 = max(abs(a1), abs(b1))
        p2 = min(abs(a1), abs(b1))
        g = gcd(p1, p2)
        a1 = int(a1 / g)
        b1 = int(b1 / g)
        if a1 < 0:
            a1 *= -1
            b1 *= -1

        aux = (b * a1) - (a * b1)

        if a1 == 0:
            lineas1.add(a)
        elif b1 == 0:
            lineas2.add(b)
        else:
            if (a1, b1) in caca:
                caca[(a1, b1)].add(aux)
            else:
                caca[(a1, b1)] = set()
                caca[(a1, b1)].add(aux)
            lineas.add((a1, b1, aux))

sol = 0
aux = len(lineas)
sol += int(aux * (aux - 1) / 2)
sol += aux * (len(lineas1) + len(lineas2))
sol += len(lineas1) * len(lineas2)
for a in caca.keys():
    aux = len(caca[a])
    #print(a, caca[a], aux)
    sol -= int(aux * (aux - 1) / 2)
print(sol)
