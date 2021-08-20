(n, s) = [int(x) for x in input().split()]
ordenes = {}
for i in range(n):
    (d, p, q) = input().split()
    head = d + ' ' + p
    (p, q) = (int(p), int(q))
    if head not in ordenes:
        ordenes[head] = 0
    ordenes[head] += q
ventas = {}
compras = {}
for i in ordenes:
    if i[0] == 'B':
        compras[int(i[2:])] = str(ordenes[i])
    else:
        ventas[int(i[2:])] = str(ordenes[i])
listacompras = list(compras.keys())
listaventas = list(ventas.keys())
listacompras.sort(reverse=True)
listaventas.sort(reverse=True)
for i in range(-s, 0):
    if i < -len(ventas):
        continue
    print('S ' + str(listaventas[i]) + ' ' + str(ventas[listaventas[i]]))
for i in range(s):
    if i >= len(compras):
        break
    print('B ' + str(listacompras[i]) + ' ' + str(compras[listacompras[i]]))
