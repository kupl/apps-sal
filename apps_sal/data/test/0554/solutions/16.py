n, m = map(int, input().split())
v = list(map(int, input().split()))
ans = 0
for i in range(m):
	a, b = map(int, input().split())
	ans = max(ans, sum(v[a - 1: b]) + ans)
print(ans)
