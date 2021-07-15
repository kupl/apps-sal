'''input
6
13 52 0 13 26 52
'''
from sys import stdin
import math


# main starts
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))
aux = []
mx = max(arr)
for i in arr:
	aux.append(mx - i)

g = aux[0]
for i in range(1,len(aux)):
	g = math.gcd(g, aux[i])

p = 0
for i in aux:
	p += i // g
print(p, g)
