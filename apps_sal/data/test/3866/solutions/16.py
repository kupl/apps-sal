n = int(input())

if n % 2 == 0:
    print(-1)
else:
    lista = list(range(n))
    saida = list([(2*x)%n for x in lista])
    print(' '.join(map(str, lista)))
    print(' '.join(map(str, lista)))
    print(' '.join(map(str, saida)))

