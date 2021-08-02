import sys

n_borrow = sys.stdin.readline().split()
n = int(n_borrow[0])
borrow = int(n_borrow[1])
lista = sys.stdin.readline().split()
for i in range(n):
    lista[i] = int(lista[i])

mayordif = 0


for i in range(n - 1):
    aux = lista[i] - lista[i + 1]
    if aux > mayordif:
        mayordif = aux

if mayordif == 0:
    print(0)
else:
    if mayordif < borrow:
        print(0)
    else:
        print(mayordif - borrow)
