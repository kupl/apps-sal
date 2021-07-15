from math import pi
n = int(input())
secuencia = [None] * n
maximo_to = -1
for num in range(n):
    r, h = (int(x) for x in input().strip().split())
    secuencia[num] = [r * r * h, num + 1]
secuencia.reverse()
secuencia.sort(key=lambda x: x[0])
actual = 0
bit = [0] * (n + 1)

def max_x(x, l):
    suma = 0
    while x != 0:
        suma = max(suma, l[x])
        x -= (x & -x)
    return suma

def update_x(x, l, max_n, val):
    while x <= max_n:
        if val > l[x]:
            l[x] = val
        else:
            return
        x += (x & -x)
for e in range(n):
    maximo = secuencia[e][0] + max_x(secuencia[e][1] - 1, bit)
    update_x(secuencia[e][1], bit, n, maximo)
    if maximo > maximo_to:
        maximo_to = maximo
print(maximo_to * pi)
