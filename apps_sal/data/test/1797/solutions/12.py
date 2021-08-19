n = int(input())
p = [int(x) - 1 for x in input().split()]
encontrados = [False] * n
ciclos = []
for i in range(n):
    if encontrados[i]:
        continue
    ciclos.append([i])
    encontrados[i] = True
    j = p[i]
    while not encontrados[j]:
        ciclos[-1].append(j)
        encontrados[j] = True
        j = p[j]
primero = max([len(x) for x in ciclos])
for i in range(n):
    if len(ciclos[i]) == primero:
        ciclos.pop(i)
        break
if ciclos:
    segundo = max([len(x) for x in ciclos])
else:
    segundo = 0
print((primero + segundo) ** 2 + sum([len(x) ** 2 for x in ciclos]) - segundo ** 2)
