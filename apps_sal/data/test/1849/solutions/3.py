n = int(input())
p = 998244353
odp = [0] * (n+1)
pote = [1] * 250000
for i in range(1,250000):
	pote[i] = (pote[i-1]*10)%p
for i in range(1,n+1):
	#odp[i]
	if i == n:
		odp[i] = 10
	else:
		brzeg = 2*pote[n-i-1]*10*9
		ile = n-i-1
		srodek_poj = 10 * 9*9 * pote[n-i-2]
		odp[i] = brzeg + ile*srodek_poj
		odp[i] = odp[i]%p
print(*odp[1:])
