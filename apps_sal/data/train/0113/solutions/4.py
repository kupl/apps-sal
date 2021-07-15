''' بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ '''
#codeforces
gi = lambda : list(map(int,input().split()))
for j in range(gi()[0]):
	a, b = gi()
	d = abs(a - b)
	print(d // 5 + (d % 5) // 2 + ((d % 5) % 2))
