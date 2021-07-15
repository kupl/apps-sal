n = int(input())
a = list(map(int, input().split()))

d = dict()
total = 0
for i in range(n):
	total += a[i]
	d[total] = 0

total = 0
ans = 0
for i in range(n):
	total += a[i]
	d[total] += 1
	ans = max(ans, d[total])

print(n - ans)
