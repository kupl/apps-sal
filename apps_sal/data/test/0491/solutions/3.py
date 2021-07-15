from math import *
n = int(input())

if (n >= 0):
	print(n)
	return

n = -n

S = str(n)

L = []

L.append(n)

if (len(S) >= 2):
	S1 = S[:len(S) - 1]
	L.append(S1)

if (len(S) >= 2):
	S1 = S[:(len(S) - 2)] + S[len(S) - 1]
	L.append(S1)

for i in range(len(L)):
	L[i] = int(L[i])

print (-1 * min(L))
