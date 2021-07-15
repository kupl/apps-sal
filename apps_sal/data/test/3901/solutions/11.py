n = int(input())
l = list(map(int, input().split()))
cnt1 = l.count(1)
if 0 < cnt1:
	print(n - cnt1)
	return
import math
m = n + 1
for i in range(n):
	g = l[i]
	for j in range(n - i):
		g = math.gcd(g, l[i + j])
		if g == 1:
			m = min(m, j)

if m == n + 1:
	print(-1)
else:
	print(m + n - 1)
