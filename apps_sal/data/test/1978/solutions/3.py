n = int(input())

nei = []
for _ in range(n):
	s = input()
	nei.append(list(int(c) for c in s))

m = int(input())

p = list([int(x)-1 for x in input().split()])

shortest = []
for i in range(n):
	vals = []
	for j, con in enumerate(nei[i]):
		if i==j:
			vals.append(0)
		elif con:
			vals.append(1)
		else:
			vals.append(10**6)
	shortest.append(vals)

for k in range(n):
	for i in range(n):
		for j in range(n):
			shortest[i][j] = min(shortest[i][j], shortest[i][k] + shortest[k][j])

seq = [p[0]]
dist = 0
for prev, cur in zip(p, p[1:]):
	dist += shortest[prev][cur]
	if shortest[seq[-1]][cur] < dist:
		dist = shortest[prev][cur]
		seq.append(prev)
seq.append(p[-1])

print(len(seq))
print(*[val+1 for val in seq])
