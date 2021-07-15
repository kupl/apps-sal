def main(a, b, x, y):
	sol = max(max(x, a-x-1)*b, max(y, b-y-1)*a)
	print(sol)

n = int(input())
for _ in range(n):
	lst = list(map(int, input().split()))
	a, b, x, y = lst[0], lst[1], lst[2], lst[3]
	main(a, b, x, y)

