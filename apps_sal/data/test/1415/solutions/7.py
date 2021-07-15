A, B, C, D = input().split()
a = int(A)
b = int(B)
c = int(C)
d = int(D)
lista = [[0 for i in range(555)] for j in range(555)]
c -= 1
d -= 1
lista[c][d] = 1
s = input()
k = len(s)
l = 1
print("1 ", end = "")
for i in range(k):
	if i + 1 == k:
		print(a * b - l)
		break
	if s[i] == 'U':
		if c:
			c -= 1
	elif s[i] == 'D':
		if c < a-1:
			c += 1
	elif s[i] == 'R':
		if d < b - 1:
			d += 1
	else:
		if d:
			d -= 1
	if lista[c][d] == 0:
		print("1 ", end = "")
		l += 1
	else:
		print("0 ", end = "")
	lista[c][d] = 1
	

