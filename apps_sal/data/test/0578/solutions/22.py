# CodeforcesB.py
leer = input()
leer = leer.split("e")
listo = 0
# Despues de la e
numero = int(leer[1])

# Antes del punto
valor = leer[0]
valor = valor.split(".")

if len(valor[1]) < numero:
    tamIni = len(valor[1])
    for i in range(0, numero - tamIni):
        valor[1] += "0"

aux = valor[1][0:numero]
aux2 = valor[1][numero:len(valor[1])]

for i in range(0, len(aux2)):
    if aux2[i] == "0":
        Cero = True
    else:
        Cero = False
        break

if aux2:
    if Cero == False:
        resultado = str(valor[0]) + str(aux) + "." + str(aux2)
    else:
        resultado = str(valor[0]) + str(aux)
else:
    resultado = str(valor[0]) + str(aux)

for i in range(0, len(resultado)):
    if resultado[i] == "0":
        Cero = True
    else:
        Cero = False
        break

if Cero == True:
    print("0")
else:
    print(resultado)
