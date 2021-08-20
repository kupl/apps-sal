import sys
n_d = sys.stdin.readline().split()
n = int(n_d[0])
d = int(n_d[1])
lista = sys.stdin.readline().split()
for i in range(n):
    lista[i] = int(lista[i])
m = int(sys.stdin.readline())
count = 0
lista = sorted(lista)
lista.reverse()
while m > 0:
    if len(lista) > 0:
        count += lista.pop()
    else:
        count -= d
    m -= 1
print(count)
