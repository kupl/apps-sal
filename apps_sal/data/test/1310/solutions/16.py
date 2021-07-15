n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
	for j in range(i,n):
		cur = 0
		for k in range(i,j + 1):
			cur ^= a[k]
		ans = max(ans, cur)
print(ans)
