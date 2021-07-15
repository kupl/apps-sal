n, c = 0, 0
def dfs(now, m, t):
	nonlocal n, c
	if now == 0:
		if m > n:
			n, c = m, t
		return
	i = 1
	while i**3 <= now:
		i += 1
	i -= 1
	dfs(now-i**3, m+1, t+i**3)
	dfs(i**3-1-(i-1)**3, m+1, t+(i-1)**3)
m = int(input())
dfs(m, 0, 0)
print(n, c)

