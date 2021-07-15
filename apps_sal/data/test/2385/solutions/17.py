import sys
sys.setrecursionlimit(1234567890)

n, *L = map(int, open(0).read().split())
mod = 10 ** 9 + 7
con = [[] for _ in range(n + 1)]
sz = [1] * (n + 1)
par = [0] * (n + 1)

for s, t in zip(*[iter(L)] * 2):
	con[s] += t,
	con[t] += s,


def prepare(m, mod=10 ** 9 + 7):
	fac = [1] * (m + 1)
	inv = [1] * (m + 1)
	for i in range(1, m + 1):
		fac[i] = fac[i - 1] * i % mod
	inv[-1] = pow(fac[-1], mod - 2, mod)
	for i in range(m - 1, -1, -1):
		inv[i] = inv[i + 1] * (i + 1) % mod
	return fac, inv


fac, inv = prepare(n)


def dfs1(cur, pre):
	par[cur] = pre
	for nxt in con[cur]:
		if nxt != pre:
			dfs1(nxt, cur)
			sz[cur] += sz[nxt]
			dp1[cur] *= dp1[nxt] * inv[sz[nxt]] % mod
			dp1[cur] %= mod
	dp1[cur] *= fac[sz[cur] - 1]
	dp1[cur] %= mod


def dfs2(cur, pre):
	dp2[cur] *= dp1[cur] * inv[sz[cur] - 1] % mod
	dp2[cur] %= mod
	dp2[cur] *= fac[n - 1]
	dp2[cur] %= mod
	for nxt in con[cur]:
		if nxt != pre:
			dp2[nxt] = fac[sz[nxt]] * pow(n - sz[nxt], mod - 2, mod) * pow(dp1[nxt], mod - 2, mod) * dp2[cur] * inv[n - 1] % mod
			dfs2(nxt, cur)


dp1 = [1] * (n + 1)
dfs1(1, 0)
dp2 = [1] * (n + 1)
dfs2(1, 0)

print(*dp2[1:], sep="\n")

