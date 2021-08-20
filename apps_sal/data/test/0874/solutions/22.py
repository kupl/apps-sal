n = int(input())
p = list(range(1, n + 1))
if n % 2 == 0:
    lista = ''
    for i in range(0, n, 2):
        tmp = p[i + 1]
        p[i + 1] = p[i]
        p[i] = tmp
    for item in p:
        lista += str(item) + ' '
    print(lista)
else:
    print(-1)
