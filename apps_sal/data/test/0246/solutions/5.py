def f(x):
	ans = x
	while x > 0:
		ans -= x % 10
		x //= 10
	return ans
n, s = list(map(int, input().split()))
if f(n) < s:
	print(0)
	return
l, r = 1, n
while l < r:
	m = (l + r) // 2
	if f(m) >= s:
		r = (m // 10) * 10
	else:
		l = m + 1
print(n - l + 1)

