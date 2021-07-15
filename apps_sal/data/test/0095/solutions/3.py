n = int(input())
a = list(map(int, input().split()))

d = [a[i] - a[i - 1] for i in range(1, n)]

# print(d)

for i in range(len(d) - 1):
	if d[i] <= 0 and d[i + 1] > 0:
		print('NO')
		return
	if d[i] < 0 and d[i + 1] == 0:
		print('NO')
		return

print('YES')

