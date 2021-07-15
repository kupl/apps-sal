k, r = map(int, input().split())
ans = 1
while ((ans * k) % 10 != r) and ((ans * k) % 10 != 0):
	ans += 1
print(ans)
