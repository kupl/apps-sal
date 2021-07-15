ways = [0] * 5001
s_ways = [0] * 5001
n = int(input())
a = set(map(int, input().split()))

for diff in range(4999, 0, -1):
	for i in a:
		if i >= diff and (i - diff in a):
			ways[diff] += 1
	ways[diff] /= (n * (n - 1) / 2)
	s_ways[diff] = s_ways[diff + 1] + ways[diff]

ans = 0
for diff1 in range(1, 5000):
	for diff2 in range(1, 5000 - diff1):
		targetdiff = diff1 + diff2 + 1
		ans += ways[diff1] * ways[diff2] * s_ways[targetdiff]

print(ans)
