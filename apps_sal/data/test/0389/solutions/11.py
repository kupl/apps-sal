a, b = list(map(int, input().split()))
res = 0

for x in (2, 3, 5):
	while a % x == 0 and b % x == 0:
		a //= x
		b //= x
	while a % x == 0:
		a //= x
		res += 1
	while b % x == 0:
		b //= x
		res += 1

if a == b:
	print(res)
else:
	print(-1)

