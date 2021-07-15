n = int(input())
x = list(map(int, input().split()))
res = 0
for i in range(1, n - 1):
	if (x[i] > x[i - 1] and x[i] > x[i + 1]) or (x[i] < x[i - 1] and x[i] < x[i + 1]):
		res += 1
print(res)		

