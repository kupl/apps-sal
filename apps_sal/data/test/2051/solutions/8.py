from collections import Counter, defaultdict

class DSU:
	def __init__(self, n):
		self.parents = [i for i in range(n)]
		self.rank = [0 for i in range(n)]

	def find_parent(self, a):
		if a == self.parents[a]:
			return a
		else:
			b = self.find_parent(self.parents[a])
			self.parents[a] = b
			return b

	def join_sets(self, a, b):
		a = self.find_parent(a)
		b = self.find_parent(b)
		if a != b:
			if self.rank[a] < self.rank[b]:
				a, b = b, a
			self.parents[b] = a
			if self.rank[a] == self.rank[b]:
				self.rank[a] += 1

n, m, k = map(int, input().split(' '))
dsu = DSU(n)
colors = list(map(int, input().split(' ')))
for _ in range(m):
	a, b = map(int, input().split(' '))
	a, b = a-1, b-1
	dsu.join_sets(a, b)
cur_colors = defaultdict(Counter)
for i in range(n):
	cur_colors[dsu.find_parent(i)][colors[i]] += 1
ans = 0
for color_counter in cur_colors.values():
	ans += sum(color_counter.values()) - color_counter.most_common(1)[0][1]

print(ans)
