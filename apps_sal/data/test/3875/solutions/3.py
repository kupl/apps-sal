MOD = 10**9+7
from itertools import product
from bisect import bisect
from collections import Counter

def lis(N, A):
	INF = 1000
	dp = [INF]*(N+1)
	dp[0] = -1
	for a in A:
		idx = bisect(dp, a-1)
		dp[idx] = min(a, dp[idx])
	return max(i for i in range(N+1) if dp[i] < INF)	

def multisigma(n, x):
	res = 1
	for i in range(n):
		res *= x - i
		res *= pow(i+1, MOD-2, MOD)
		res %= MOD
	return res

def dfs(R, num, tmp):
	nonlocal ans
	#print(R, num, tmp)
	n = len(R)
	if tmp == n:
		#print(R, lis(n, R))
		ans += num * lis(n, R)
		ans %= MOD
		return
	l = len(space[tmp])
	if l == 0:
		dfs(R, num, tmp+1)
		return
	for P in product(range(l), repeat=l):
		P = list(P)
		m = len(set(P))
		if m != max(P) + 1:
			continue
		if m > zone[tmp]:
			continue
		for x, y in zip(P, space[tmp]):
			R[y] = x + tmp * 10
		nxt = (num * multisigma(m, zone[tmp])) % MOD
		dfs(R, nxt, tmp+1)
	return

n = int(input())
a = list(map(int, input().split()))
b = sorted(list(set(a)))
zone = [b[0]]
for i in range(1, len(b)):
	zone.append(b[i] - b[i-1])
d = dict()
tmp = 0
h = [-1 for _ in range(n)]
for i, z in enumerate(zone):
	tmp += z
	d[tmp] = i
for i, x in enumerate(a):
	h[i] = d[x]
#print(h)
k = len(zone)
ans = 0
for P in product(range(k), repeat=n):
	ok = True
	P = list(P)
	for i, p in enumerate(P):
		if p > h[i]:
			ok = False
			break
	if not ok:
		continue
	space = [[] for _ in range(n)]
	for i, p in enumerate(P):
		space[p].append(i)
	c = Counter(P)
	R = [-1 for _ in range(n)]
	dfs(R, 1, 0)
for x in a:
	ans *= pow(x, MOD-2, MOD)
	ans %= MOD
print(ans)
