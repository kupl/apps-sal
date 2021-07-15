n = int(input())
arr = [*map(int, input().split())]

arr.sort()
x = int(arr[-1] ** (1 / (n - 1)))
y = x + 1
ans = res = 0

for i, j in zip(arr, range(n)):
	ans += abs(i - (x ** j))
	res += abs(i - (y ** j))

print(min(ans, res))
