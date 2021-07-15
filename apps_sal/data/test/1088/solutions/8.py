import sys
def input():
	return sys.stdin.readline()[:-1]

class UnionFind():
	def __init__(self, size):
		self.table = [-1 for _ in range(size)]
		self.size = [1 for _ in range(size)]

	def find(self, x):
		while self.table[x] >= 0:
			if self.table[self.table[x]] >= 0:
				self.table[x] = self.table[self.table[x]]
			x = self.table[x]
		return x

	def same(self, x, y):
		return self.find(x) == self.find(y)

	def unite(self, x, y):
		s1 = self.find(x)
		s2 = self.find(y)
		if s1 != s2:
			r1 = self.table[s1]
			r2 = self.table[s2]
			if r1 <= r2:
				self.table[s2] = s1
				if r1 == r2:
					self.table[s1] -= 1
				self.size[s1] += self.size[s2]
				self.size[s2] = 0
			else:
				self.table[s1] = s2
				self.size[s2] += self.size[s1]
				self.size[s1] = 0
		return

MOD = 998244353
n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 1

uf_t = UnionFind(n)
uf_y = UnionFind(n)

for s in range(1, n):
	for t in range(s):
		ok_y, ok_t = True, True
		for i in range(n):
			if a[s][i] + a[t][i] > k:
				ok_y = False
			if a[i][s] + a[i][t] > k:
				ok_t = False
		if ok_y:
			uf_y.unite(s, t)
		if ok_t:
			uf_t.unite(s, t)

fact = [1 for _ in range(51)]
for i in range(1, 51):
	fact[i] = (fact[i-1] * i) % MOD

for i in range(n):
	if uf_t.size[i] > 0:
		ans *= fact[uf_t.size[i]]
		ans %= MOD
	if uf_y.size[i] > 0:
		ans *= fact[uf_y.size[i]]
		ans %= MOD

print(ans)
