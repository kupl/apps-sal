n = int(input())
lista = input().split()
p = int(lista[0])
q = int(lista[0])
for i in range(1, n):
    k = int(lista[i])
    if k <= p:
        p = k
    elif k >= q:
        q = k
print(int(q - p))
