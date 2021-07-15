n_k = input()
n_k = n_k.split(" ")

n = int(n_k[0])
k = int(n_k[1])

ais = input()
ais = ais.split(" ")

q = int(input())

pares = {}

for a in ais:
    a = int(a)
    for i in range(k):
        p = int((i+1)*a)
        if (p not in pares) or (i+1 < pares[p]):
            pares[p] = i+1

m = 1000000000

for i in range(q):
	x = int(input())
	ans = 1000;

	minimo = m
	for plata, deuda in list(pares.items()):
		if plata == x:
			if deuda <= k:
				if deuda < minimo:
					minimo = deuda
		else:
			r = x-plata
			if r in pares:
				if deuda+pares[r] < minimo:
					if deuda + pares[r] <= k:
						minimo = deuda+pares[r]
	if minimo == m:
		print(-1)
	else:
		print(minimo)
# 1538793706889

