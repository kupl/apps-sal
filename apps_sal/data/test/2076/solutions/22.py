t = int(input())
for i in range(t):
	a, b, c = map(int, input().split())
	if b == 0:
		print(0)
	else:
		res = 0
		res += 3 * min(b, c // 2)
		b -= res // 3
		res += 3 * min(a, b // 2)
		print(res)
