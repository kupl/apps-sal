tab = [1,3]
for i in range(100):
	xx = tab[-1]
	tab.append(xx + 2**(i+2))

t = int(input())
for rew in range(t):
	n = int(input())
	wyn = -1
	for j in tab:
		if n%j == 0 and j > 1:
			wyn = n//j
			break
	print(wyn)
