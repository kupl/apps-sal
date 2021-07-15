# -*-coding: utf-8 -*-

# Inicio del Programa
n, k = [int(x) for x in input().split()]
numeros = [int(x) for x in input().split()]

numeros.sort()
suma = sum(numeros[:k])
print(suma)

