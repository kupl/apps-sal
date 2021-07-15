from math import log

def f(n):
	l = int(log(n + 1, 2)) - 1
	n0 = n - 2**(l + 1) + 1
	x = 0
	y = 0
	for i in range(l + 1):
		if i % 2 == 0:
			x += 2**(i)
		else:
			y += 2**(i)
	if l % 2 != 0:
		x += n0
	else:
		y += n0
	return (x, y)

MOD = 10**9 + 7
l, r = map(int, input().split())
L = f(l - 1)
R = f(r)
x1, y1 = L
x2, y2 = R
ans = 0
ans += x2**2 % MOD
ans -= x1**2 % MOD
ans += y2*(y2 + 1) % MOD
ans -= y1*(y1 + 1) % MOD
print(ans % MOD)
