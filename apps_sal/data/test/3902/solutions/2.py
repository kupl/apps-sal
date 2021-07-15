from sys import *
setrecursionlimit(20000)
dp = []
ans = []
def fun(s, pos, r, ln):
	if pos <= 4+ln:
		return 0
	if dp[pos][ln-2] != 0:
		return dp[pos][ln-2]
	if s[pos-ln:pos] != r:
		dp[pos][ln-2] = 1 + fun(s, pos - ln, s[pos-ln:pos],2) + fun(s, pos - ln, s[pos-ln:pos],3)
		ans.append(s[pos-ln:pos])
	'''	if pos > 4+ln and s[pos-3:pos] != r:
		dp[pos][1] = 1 + fun(s, pos - 3, s[pos-3:pos])
		ans.append(s[pos-3:pos])'''
	return dp[pos][ln-2]


s = input()
dp = [[0, 0] for i in range(len(s) + 1)]
fun(s, len(s), '', 2)
fun(s, len(s), '', 3)
ans = list(set(ans))
ans.sort()
print(len(ans))
for i in ans:
	print (i)

