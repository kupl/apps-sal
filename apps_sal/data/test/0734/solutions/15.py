n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
a.sort()
ans = 0
h = a[-1]
for i in range(n, 0, -1):
	if a[i - 1] < h - 1:
		ans = ans + a[i] - h + a[i - 1]
		h = a[i - 1]
	else:
		ans = ans + a[i] - 1
		h = h - 1
print(ans)
