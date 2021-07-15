import sys

n = int(input())

f = [int(x) for x in input().split(' ')]

image = set()

h = []

for i, x in enumerate(f):
	if x not in image:
		image.add(x)
		h.append(x)

inv_h = [None for _ in range(n+1)]

for i, x in enumerate(h, 1):
	inv_h[x] = i

for val in h:
	if f[val-1] != val:
		print(-1)
		return

print(len(h))

g = [None for _ in range(n)]

for i in range(n):
	g[i] = inv_h[f[i]]

for x in g:
	print(x, end=' ')
print('')

for x in h:
	print(x, end=' ')
print('')





