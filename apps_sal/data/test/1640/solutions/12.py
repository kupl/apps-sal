n = int(input())
cnt = {}
res = 0
s = 0
a = list(map(int, input().split()))
for i in range(n):
	x = a[i]
	s += x
	cnt[x] = cnt.get(x, 0) + 1
	res += x * (i + 1 - (cnt.get(x, 0) + cnt.get(x - 1, 0) + cnt.get(x + 1, 0))) - (s - (x * cnt.get(x, 0) + (x - 1) * cnt.get(x - 1, 0) + (x + 1) * cnt.get(x + 1, 0)))
print(res)
