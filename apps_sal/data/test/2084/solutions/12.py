# -*-coding: utf-8 -*-
from sys import stdin
for line in stdin:
    entrada = line.splitlines()
    break
n = int(entrada[0].split()[0])
k = int(entrada[0].split()[1])
numeros = [int(x) for x in input().split()]
numeros.sort()
suma = sum(numeros[:k])
print(suma)
