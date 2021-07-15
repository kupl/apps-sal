n, k, x = list(map(int, input().split()))
a = list(map(int, input().split()))
res = 0
for i in range(n - k):
	res += a[i]
print(res+ k * x)

