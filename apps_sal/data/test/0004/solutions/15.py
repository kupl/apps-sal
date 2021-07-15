def dst(a, b):
	if (a <= b):
		return b - a
	return b - a + 60 * 24

x = int(input())
h, m = map(int, input().split())
# print(h, m)
cur = 60 * h + m
ans = 10**9
for H in range(24):
	for M in range(60):
		if (str(H) + str(M)).count("7"):
			if (dst(H * 60 + M, cur) % x == 0):
				ans = min(ans, dst(H * 60 + M, cur) // x)
print(ans)
