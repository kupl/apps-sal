def solve(l, costs):
	ans = 0
	for i in range(31, -1, -1):
		if ((l >> i) & 1) == 1:
			ans += min(costs[i + 1], costs[i] + solve(l - ex(2, i), costs))
			break
	return ans

def ex(base, exp):
	ans = 1
	for i in range(exp):
		ans = ans * base
	return ans

n, l = str(input()).split(' ')
n, l = int(n), int(l)

costs = str(input()).split(' ')
costs = [int(c) for c in costs]

for i in range(1, n):
	costs[i] = min(costs[i], 2 * costs[i - 1])
	
for i in range(len(costs), 32):
	costs.append(2 * costs[i - 1])

for i in range(30, -1, -1):
	costs[i] = min(costs[i], costs[i + 1])
	
print(solve(l, costs))

