def costo(a, b, t):
    resultado = 0
    for elem in a:
        resultado += max(t - elem, 0)
    for elem in b:
        resultado += max(elem - t, 0)
    return resultado


m, n = tuple(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

inf, sup = min(a), max(b)
while inf < sup:
    t = (inf + sup)//2
    if costo(a, b, t+1) - costo(a, b, t) >= 0:
        sup = t
    else:
        inf = t + 1

print(costo(a, b, inf))


