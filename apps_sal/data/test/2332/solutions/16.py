n, k, m = list(map(int, input().split()))
palabras = {x: y + 1 for y, x in enumerate(input().split())}
costos = [int(x) for x in input().split()]
traspasos = [x for x in range(n + 1)]
costos_minimos = costos[:]
for e in range(k):
    lista = [int(x) for x in input().split()]
    lista.pop(0)
    m = 10 ** 10
    for q in lista:
        if costos[q - 1] < m:
            m = costos[q - 1]
    for q in lista:
        costos_minimos[q - 1] = m
mensaje = input().split()
suma = 0
for e in mensaje:
    suma += costos_minimos[palabras[e] - 1]
print(suma)

