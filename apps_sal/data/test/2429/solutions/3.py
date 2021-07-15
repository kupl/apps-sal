pot = [1] * 40
for i in range(1,40):
	pot[i] = 2 * pot[i-1]
q = int(input())
for riwe in range(q):
	n = int(input())
	wyn = pot[n]
	for i in range(n//2):
		j = n-1-i
		wyn -= pot[j]
	for i in range(1,n//2):
		wyn += pot[i]
	print(wyn)
