import math
def combinations_count(n, r):
	if n < 2:
		return 0
	return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
  
n = int(input())
aa = [int(i) for i in input().split()]
d = {}
for a in aa:
	d[a] = d.get(a, 0) + 1
kei = 0
for k in d.keys():
	combi = combinations_count(d[k], 2)
	kei += combi
	d[k] = (d[k], combi)
ret = 0
for k in d.keys():
	d[k] = (d[k][0], d[k][1], kei - d[k][0] + 1)
for a in aa:
	print(d[a][2])
