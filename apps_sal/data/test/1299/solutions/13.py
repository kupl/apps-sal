n, k = (int(x) for x in input().split())
x = [int(x) for x in input().split()]

s = [0]
for i in range(n):
	s.append(s[i] + x[i])

a = n - k - k + 1
sa = s[n - k] - s[a - 1]
b = n - k + 1
sb = s[n] - s[b - 1]
ans = sa + sb
ansa = a
ansb = b
ib = b

while a > 1:
	a -= 1
	sa = s[a + k - 1] - s[a - 1]
	b -= 1
	tb = s[b + k - 1] - s[b - 1]
	if tb >= sb:
		sb = tb
		ib = b
	if sa + sb >= ans:
		ansa = a
		ansb = ib
		ans = sa + sb

print(ansa, ansb)

