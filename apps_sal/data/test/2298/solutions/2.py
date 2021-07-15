from sys import stdin
input = stdin.readline
t = int(input())
for _ in range(t):
	a,b,q = map(int,input().split())
	przyg = [0] * (a*b)
	for i in range(a*b):
		if (i%a)%b != (i%b)%a:
			przyg[i] = 1
	cyk = sum(przyg)
	pref = [0]*(a*b)
	pref[0] = przyg[0]
	for i in range(1,a*b):
		pref[i] = pref[i-1] + przyg[i]
	for query in range(q):
		l,r = map(int,input().split())
		ll = l%(a*b)
		rr = r%(a*b)
		wynik = cyk * (r//(a*b) - l//(a*b))
		wynik += pref[rr]
		if ll > 0:
			wynik -= pref[ll-1]
		if query < q-1:
			print(wynik, end = " ")
		else:
			print(wynik)
