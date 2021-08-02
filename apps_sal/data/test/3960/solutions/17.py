lectura = lambda: map(int, input().split())
n = (list(lectura())[0])
lista = list(lectura())
fDescrita = 0
alt1 = 1
maxV1 = 0
maxV2 = 0
C1 = 0
C2 = 0
for i in range(0, n - 1):
    fDescrita = abs(lista[i] - lista[i + 1]) * alt1
    maxV1 = max(maxV1 + fDescrita, fDescrita)
    maxV2 = max(maxV2, maxV1)
    alt1 = alt1 * (-1)
    # print(fDescrita,maxV1,maxV2)
C1 = maxV2
maxV1 = 0
maxV2 = 0
alt1 = 1
for i in range(1, n - 1):
    fDescrita = abs(lista[i] - lista[i + 1]) * alt1
    maxV1 = max(maxV1 + fDescrita, fDescrita)
    maxV2 = max(maxV2, maxV1)
    alt1 = alt1 * (-1)
    # print(fDescrita,maxV1,maxV2)
C2 = maxV2
print(max(C1, C2))
