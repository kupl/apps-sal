n = int(input())
t = list(input())

def dist(a, b):
	return min((ord(a) - ord(b) + 26) % 26, (ord(b) - ord(a) + 26) % 26)

m = 'ACTG'

def solve(s):
	res = 0
	for i in range(4):
		res += dist(t[s + i], m[i])
	return res

ans = 30 * n
for s in range(n - 3):
	ans = min(ans, solve(s))

print(ans)
