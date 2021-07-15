n = int(input())
a = [int(x) for x in input().split()]

lasts = {}
for i in range(n):
	lasts[a[i]] = i

dss = {x: x for x in a}
changed = True
while changed:
	changed = False
	for i in range(1, n):
		if dss[a[i-1]] != dss[a[i]] or lasts[a[i-1]] != lasts[a[i]]:
			if lasts[a[i-1]] >= i:
				changed = True
				lasts[a[i-1]] = lasts[a[i]] = max(lasts[a[i-1]], lasts[a[i]])
				dss[a[i-1]] = dss[a[i]] = min(dss[a[i-1]], dss[a[i]])

M = 998244353

def powmod(x, p, m = M):
	if x == 0:
		return 0
	if p == 0:
		return 1
	return (powmod(x*x, p//2)%m) * (x if p%2 == 1 else 1) % m

kinds = len(set(dss.values()))
ans = powmod(2, kinds-1)

#print(n, a, dss, lasts, kinds)
#print([powmod(2, i, 13) for i in range(10)])

print(ans)
