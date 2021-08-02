x, n, k = [int(x) for x in input().split()]
lista = [int(x) for x in input().split()]
acumuladaL = []
acumuladaR = []
mult = k ** n

cont = 0
for i in lista:
    cont |= i
    acumuladaL.append(cont)
cont = 0
for i in lista[::-1]:
    cont |= i
    acumuladaR.append(cont)
if len(lista) == 1:
    print(lista[0] * mult)
elif len(lista) == 2:
    acumuladaR = acumuladaR[::-1]
    maximo = max([lista[0] * mult | acumuladaR[1],
                  lista[-1] * mult | acumuladaL[-2]])
    print(maximo)
else:
    maximo = max([lista[0] * mult | acumuladaR[1], lista[-1] * mult | acumuladaL[-2]])
    acumuladaR = acumuladaR[::-1]

    for i in range(1, len(lista) - 1):
        var = lista[i] * mult | acumuladaR[i + 1] | acumuladaL[i - 1]
        if maximo < var:
            maximo = var
    print(maximo)

# 1500336849347
