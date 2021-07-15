from math import sqrt

def phi(u):
	ans = u
	for i in range(2, int(sqrt(n)) + 1):
		if u % i == 0:
			while u % i == 0:
				u = u / i
			ans = ans - int(ans / i)
	if n > 1:
		ans = ans - int(ans / n)
	return ans

def binpow(u, a, mod):
	ans = 1
	if a == 0:
		return 1;
	while a > 0:
		if a % 2 == 0:
			u = (u ** 2) % mod
			a = int(a / 2)
		else :
			ans = (ans * u) % mod
			a = a - 1
	return int(ans)

def ffind(s, u):
	if u == 0:
		return -1;
	ans = -1;
	while u > 0:
		ans = s.find('1', ans + 1)
		u = u - 1
	return ans

n = int(input())

while n > 0:
	k = int(input())
	ss = input().split(' ')
	s = ''
	for i in ss:
		s = s + i
	mx = 1000000000
	u = s.count('1')	
	for i in range(7):
		d = s[i:].count('1')
		ans = 0
		if d >= k:
			ans = ffind(s[i:], k) + 1
		else :
			dd = int((k-d)/u)
			ans = 7 - i + 7 * dd + ffind(s, k - d - dd * u) + 1
			if k == d + dd * u:
				ans = ans - s[-1::-1].find('1')

		mx = min(mx, ans)

	print(mx)
	n = n - 1
