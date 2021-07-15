a, b = (int(x) for x in input().split())
ans = 0
while b:
	ans += a // b
	a %= b
	a, b = b, a
print(ans)

