n = int(input())
maior = 0
m = 0
banco = 0
for i in range(n):
    a = input().split('\n')
    a = a[0].split(' ')
    s = int(a[0])
    a.pop(0)
    lista = []
    for j in a:
        lista.append(int(j))
    lista.sort(reverse=True)

    if i == 0:
        maior = lista[0]
    if maior > lista[0]:
        banco += (maior - lista[0]) * s
    elif maior < lista[0]:
        banco += (lista[0] - maior) * m
        maior = lista[0]
    m += s
print(banco)
