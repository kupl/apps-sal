import sys
flag = 0
sereja = 0
dima = 0
n = int(sys.stdin.readline())
lista = sys.stdin.readline().split()
for i in range(n):
    lista[i] = int(lista[i])
actual = 0
while len(lista) > 0:
    if len(lista) == 1:
        actual = lista.pop()
    elif lista[0] > lista[-1]:
        actual = lista.pop(0)
    else:
        actual = lista.pop()
    if flag == 0:
        sereja += actual
        flag = 1
    else:
        dima += actual
        flag = 0
print(sereja, ' ', dima)
