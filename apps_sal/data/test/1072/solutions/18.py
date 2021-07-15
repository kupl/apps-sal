s = input()
s = s.split()
n = int(s[0]) # Linhas
m = int(s[1]) # Colunas
l = []

for i in range(0,n):
	s = input()
	l.append(s)

cont = 0

ant = 0
i = 0
while (i < n):
	if (l[ant] > l[i]):
		for k in range(0, n):
			l[k] = list(l[k])

		for j in range(0, m):
			if (l[ant][j] > l[i][j]):
				break

		for k in range(0, n):
			l[k].pop(j)
			l[k] = "".join(l[k])

		i = 0
		ant = 0
		m -= 1
		cont += 1

	else: 
		ant = i
		i += 1

print(cont)
