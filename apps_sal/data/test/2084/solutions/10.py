(n, k) = [int(x) for x in input().split()]
numeros = [int(x) for x in input().split()]
numeros.sort()
suma = sum(numeros[:k])
print(suma)
