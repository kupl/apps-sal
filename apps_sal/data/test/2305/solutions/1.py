import sys
sys.setrecursionlimit(10**6)
def input():
	return sys.stdin.readline()[:-1]

n = int(input())
c = list(map(int, input().split()))
ans = [n*(n+1)//2 for _ in range(n)]
for i in range(n):
	c[i] -= 1
adj = [[] for _ in range(n)]
for _ in range(n-1):
	a, b = map(int, input().split())
	adj[a-1].append(b-1)
	adj[b-1].append(a-1)

s = 0
dp = [0 for _ in range(n)]

def dfs(x, p):
	nonlocal s
	pres = s + dp[c[x]]
	for v in adj[x]:
		if v == p:
			continue
		dp[c[x]] = -s
		dfs(v, x)
		ans[c[x]] -= (s+dp[c[x]]) * (s+dp[c[x]]+1) // 2
	s += 1
	dp[c[x]] = pres - s
	return

dfs(0, -1)
for i in range(n):
	ans[i] -= (s+dp[i]) * (s+dp[i]+1) // 2

print(*ans, sep="\n")
