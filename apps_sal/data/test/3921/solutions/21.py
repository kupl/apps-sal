n = int(input())
inf = 200001

p = [0] * inf
a = [[] for _ in range(inf)]

a[1] = [1]

for i in range(2, inf):
	a[i].append(i)
	for j in range(i * 2, inf, i):
		a[j].append(i)
for i in map(int, input().split()):
	mx = max(p[j] for j in a[i]) + 1
	for j in a[i]:
		p[j] = mx
print(max(p))

