import math
import sys

def Cmmdc(a, b):
	r = 0
	while b > 0:
		r = a % b
		a = b
		b = r
	return a

lst = list(map(int, input().split()))

t = auxT = lst[0]
n = lst[1]
m = lst[2]

if n > m:
	aux = n
	n = m
	m = aux

cmmdc = Cmmdc(n, m)
cmmmc = n * m // cmmdc

fav = (t // cmmmc) * n
t = t % cmmmc
fav += min(n - 1, t)

t = auxT
c = Cmmdc(fav, t)
fav //= c
t //= c

print(str(fav) + "/" + str(t) + "\n")

