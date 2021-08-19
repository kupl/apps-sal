lista = list(map(int, input().split()))
lista.sort()
count = 0
A = lista[0]
B = lista[1]
C = lista[2]
while A != B or B != C or C != A:
    if C - A >= 2:
        lista[0] += 2
    else:
        lista[0] += 1
        lista[1] += 1
    lista.sort()
    A = lista[0]
    B = lista[1]
    C = lista[2]
    count += 1
print(count)
