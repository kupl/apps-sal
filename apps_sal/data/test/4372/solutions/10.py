ll = lambda:list(map(int, input().split()))
from fractions import gcd
from functools import reduce
def find_gcd(list):
    x = reduce(gcd, list)
    return x
testcases = 1
# [testcases] = ll()
for _ in range(testcases):
	[n] = ll()
	a = ll()
	amax = max(a)
	l = []
	ans = 0
	for x in range(n):
		if not amax ==a[x]:
			# ans +=(amax-a[x])
			l.append(amax-a[x])
	h = find_gcd(l)
	# print(h)
	for x in range(n):
		if not amax ==a[x]:
			ans+=((amax-a[x])//h)
	print(ans,h)

