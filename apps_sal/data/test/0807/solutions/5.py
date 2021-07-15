n, c = list(map(int, input().split()))
x = list(map(int, input().split()))
m = 0
for i in range(len(x) - 1):
	m = max(m, x[i] - x[i + 1])
if m - c > 0:
	print(m - c)
else:
	print(0)

