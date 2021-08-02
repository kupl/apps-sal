def Posicion(L):
    i = 1
    A = L
    for k in range(len(L)):
        if L[k] != 0:
            A[k] = i
            i += 1
        else:
            i = 1
    return A


def SepararDerecha(L):
    B = []
    Mayork = 0
    for k in range(len(L)):
        if L[k] == 0:
            if k > Mayork:
                Mayork = k
    c = Mayork + 1
    while c < len(L):
        B.append(L[c])
        c += 1
    return B


def SepararIzquierda(L):
    B = []
    k = 0
    while L[k] != 0:
        B.append(L[k])
        k += 1
    return B


def Invertir(L):
    B = []
    k = len(L) - 1
    while k >= 0:
        B.append(L[k])
        k -= 1
    return B


N = int(input())
L = input()
L = L.split()
A = []
for k in range(len(L)):
    A.append(int(L[k]))
PI = SepararIzquierda(A)
z = len(PI)
PIII = []
for k in range(len(PI)):
    PIII.append(z)
    z -= 1
pizquierda = len(PIII)
PD = SepararDerecha(A)
PD = Posicion(PD)
pderecha = len(PD)
D = []
for k in range(pizquierda, len(A) - pderecha):
    D.append(A[k])
AI = Posicion(D)
AD = Invertir(D)
AD = Posicion(AD)
AD = Invertir(AD)
B = []
for k in range(len(AD)):
    if AD[k] < AI[k]:
        B.append(AD[k])
    else:
        B.append(AI[k])
C = []
for k in range(len(PIII)):
    C.append(PIII[k])
for k in range(len(B)):
    C.append(B[k])
for k in range(len(PD)):
    C.append(PD[k])
Respuesta = str(C[0])
for k in range(1, len(C)):
    Respuesta += ' ' + str(C[k])
print(Respuesta)
