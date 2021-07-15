n, m, k = map(int, input().split())
b = list(map(int, input().split()))
g = [b[i+1] - b[i] - 1 for i in range(n-1)]
g.sort(reverse=True)
ans = b[n-1] - b[0] + 1
for i in range(k-1):
	ans -= g[i]
print(ans)
