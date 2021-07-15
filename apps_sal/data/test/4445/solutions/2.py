n = int(input())
l = list(map(int,input().split()))
par = []
npar = []
for i in l:
	if i % 2 == 0:
		par.append(i)
	else:
		npar.append(i)
if abs(len(par) - len(npar)) <= 1:
	print(0)
else:
	if len(par) - len(npar) > 1:
		par = sorted(par)
		npar = sorted(npar)
		wyn = 0
		for i in range(len(par) - len(npar) - 1):
			wyn = wyn + par[i]
		print(wyn)
	if len(npar) - len(par) > 1:
		par = sorted(par)
		npar = sorted(npar)
		wyn = 0
		for i in range(len(npar) - len(par) - 1):
			wyn = wyn + npar[i]
		print(wyn)

