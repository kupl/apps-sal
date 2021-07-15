#!/usr/bin/env python3

[n, m] = list(map(int, input().strip().split()))
bis = [input().strip() for _ in range(n)]

trbis = [''.join(bis[i][j] for i in range(n)) for j in range(m)]

nec = [0 for i in range(n)]
for col in trbis:
	if col.count('1') == 1:
		nec[col.index('1')] = 1

if sum(nec) < n:
	print ('YES')
else:
	print ('NO')

