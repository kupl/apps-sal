n = int(input())
u = list(map(int, input().split()))
cnts = [0 for _ in range(10 ** 5 + 1)]
cntcnt = [10**5+1] + [0 for _ in range(10 ** 5)]
b = 1
for i in range(n):
	cnts[u[i]] += 1
	cntcnt[cnts[u[i]] - 1] -= 1
	cntcnt[cnts[u[i]]] += 1

	nz = 10 ** 5 + 1 - cntcnt[0]
	j = i + 1
	if nz == 1:
		b = j
		continue
	if j % nz == 1:
		c = j // nz
		if cntcnt[c] + 1 == nz:
			b = j
			continue

	if cntcnt[1] and (j - 1) % (nz - 1) == 0 and cntcnt[(j - 1) // (nz - 1)] == nz - 1 + (j == nz):
		b = j
print(b)
