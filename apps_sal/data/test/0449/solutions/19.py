n = int(input())
d = [100, 20, 10, 5, 1]
ans = 0
i = 0
while n > 0:
	while n < d[i]:
		i += 1
	s = n // d[i]
	ans += s
	n -= s * d[i]

print(ans)
