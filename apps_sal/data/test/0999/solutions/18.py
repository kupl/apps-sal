n = int(input())
smin = 10**9
smax = 0
for i in range(n):
	(l, r) = (int(i) for i in input().split())
	if r<smin: smin = r
	if l>smax: smax = l


m = int(input())
pmin = 10**9
pmax = 0
for i in range(m):
	(l, r) = (int(i) for i in input().split())
	if r<pmin: pmin = r
	if l>pmax: pmax = l

	
print(max(smax-pmin,pmax-smin, 0))

