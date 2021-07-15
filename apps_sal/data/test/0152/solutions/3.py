n, m, k = list(map(int, input().split()))
x, s = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
a.append(x)
b.append(0)
ans = x * n
for i in range(m + 1):
	if b[i] <= s:
		l = -1
		r = k
		while l < r - 1:
			y = l + (r - l) // 2
			if d[y] <= s - b[i]:
				l = y
			else:
				r = y
		ans1 = 0
		if l > -1:
			ans1 = a[i] * max(0, n - c[l])
		else:
			ans1 = a[i] * n
		if ans1 < ans:
			ans = ans1
print(ans)

