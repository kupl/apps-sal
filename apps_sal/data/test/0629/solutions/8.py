n = int(input())
a1 = [int(x) for x in input().split()]
a2 = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]


best, best_cross = float('inf'), -1

for i in range(n):
	tmp = sum(a1[:i]) + sum(a2[i:]) + b[i]

	if tmp < best:
		best = tmp
		best_cross = i

best2 = float('inf')
for i in range(n):
	if i == best_cross: continue

	tmp = sum(a1[:i]) + sum(a2[i:]) + b[i]

	if tmp < best2:
		best2 = tmp

print(best + best2)

