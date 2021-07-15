l, r = map(int, input().split())

mod = 2019

ans = 2222

if (r - l) // mod > 0:
	ans = 0

else:
	ans = 2020
	for i in range(l, r + 1):
		for j in range(i + 1, r + 1):
			ans = min(ans, (i % mod) * (j % mod) % mod)

print(ans)
