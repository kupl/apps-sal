mbase = 10**9+7
nof = int(input())
facts = [int(x) for x in input().split()]

pmap = {}
for p in facts:
	pmap[p] = pmap.get(p, 0) + 1

onepprod = 1
for (p, q) in pmap.items():
	onepprod*= q+1
	onepprod%= 2*(mbase-1)

res = 1
for (p, q) in pmap.items():
	res*= pow(p, (q*onepprod)//2, mbase)
	res%= mbase

print(res)
