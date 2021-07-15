import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

n, k = list(map(int, input().split()))
dp = [[0] * 2 * n for i in range(2 * n)]

require = list()

inf = int(1e5)

order = [inf] * 2 * n

for i in range(k):
	require.append(input().split())
	require[i][0] = int(require[i][0]) - 1
	if require[i][1] == '=':
		require[i][1] = '=='
	require[i][2] = int(require[i][2]) - 1

def Solve(left, right, h):
	nonlocal dp, require, order
	for element in require:
		first = order[element[0]]
		second = order[element[2]]
		string = str(first) + element[1] + str(second)
		if first == second == inf and left + 1 != right:
			continue
		if eval(string) == False:
			return 0
	if dp[left][right] != 0:
		return dp[left][right]
	if left + 1 == right:
		dp[left][right] = 1
		return 1
	order[left] = h
	order[left + 1] = h
	dp[left][right] = Solve(left + 2, right, h + 1)
	order[left + 1] = inf
	order[right] = h
	dp[left][right] += Solve(left + 1, right - 1, h + 1)
	order[left] = inf
	order[right - 1] = h
	dp[left][right] += Solve(left, right - 2, h + 1)
	order[right - 1] = inf
	order[right] = inf
	return dp[left][right]

print(Solve(0, 2 * n - 1, 0))

