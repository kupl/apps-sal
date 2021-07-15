x1, y1 = [int(x) for x in input().split()]
x2, y2 = [int(x) for x in input().split()]
n = int(input())
ans = 0
for i in range(n):
	a, b, c = [int(x) for x in input().split()]
	x = x1 * a + y1 * b + c
	x //= abs(x)
	y = x2 * a + y2 * b + c
	y //= abs(y)
	if x != y:
		ans += 1
print(ans)

