a = input('')
lista = a.split()
lista2 = []
par = 0
impar = -1
contador = 0
for i in range(int(lista[0])):
    par += 2
    lista2.append(par)
for i in range(int(lista[1])):
    impar += 2
    lista2.append(impar)
longitud = len(lista2) - 1
for i in range(0, len(lista2)):
    b = i
    while True:
        if b + 1 > longitud:
            break
        else:
            suma = lista2[i] + lista2[b + 1]
            b = b + 1
            if suma % 2 == 0:
                contador += 1
print(contador)
