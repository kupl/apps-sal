n = []
for x in range(1,10):
	n += [(2 ** x - 1) * (2 ** (x - 1))]
x = int(input())
k = []
for i in range(9):
	if x % n[i] == 0:
		k += [n[i]]
print(max(k))

