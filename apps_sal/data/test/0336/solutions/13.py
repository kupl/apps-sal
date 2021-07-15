n, a, b, c, d = map(int, input().split())

ans = 0

for x1 in range(1, n+1):
	x2 = x1+b-c
	if x2 < 1 or x2 > n:
		continue
	x4 = x1+a-d
	if x4 < 1 or x4 > n:
		continue
	x5 = x1+a+b-c-d
	if x5 < 1 or x5 > n:
		continue

	ans += 1

print(ans*n)
