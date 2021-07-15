from sys import stdin
input = stdin.readline
q = int(input())
for rwerew in range(q):
	n = int(input())
	p = list(map(int,input().split()))
	c = list(map(int,input().split()))
	for i in range(n):
		p[i] -= 1
	przyn = [0] * n
	grupa = []
	i = 0
	while i < n:
		if przyn[i] == 1:
			i += 1
		else:
			nowa_grupa = [i]
			j = p[i]
			przyn[i] = 1
			while j != i:
				przyn[j] = 1
				nowa_grupa.append(j)
				j = p[j]
			grupa.append(nowa_grupa)
	grupacol = []
	for i in grupa:
		cyk = []
		for j in i:
			cyk.append(c[j])
		grupacol.append(cyk)
	#print(grupacol)
	mini = 234283742834
	for cykl in grupacol:
		dziel = []
		d =  1
		while d**2 <= len(cykl):
			if len(cykl)%d == 0:
				dziel.append(d)
			d += 1
		dodat = []
		for d in dziel:
			dodat.append(len(cykl)/d)
		dziel_ost = list(map(int,dziel + dodat))
		#print(dziel_ost, len(cykl))
		for dzielnik in dziel_ost:
			for i in range(dzielnik):
				indeks = i
				secik = set()
				chuj = True
				while indeks < len(cykl):
					secik.add(cykl[indeks])
					indeks += dzielnik
					if len(secik) > 1:
						chuj = False
						break
				if chuj:
					mini = min(mini, dzielnik)
	print(mini)
			

