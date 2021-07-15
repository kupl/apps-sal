n = int(input())
l = []
best = [0, -1]
k = -1
for i in range(n):
	l.append([int(x) for x in input().split()])
	if l[-1][1] - l[-1][0] > best[1] - best[0]:
		best = l[-1]
		k = i
for a, b in l:
	if a < best[0] or best[1] < b:
		print(-1)
		return
print(k + 1)

