n, m = list(map(int, input().split()))
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))

MOD = 10**9 + 7
p, q = 0, 1
for i in reversed(list(range(n))):
	if s1[i] == 0 and s2[i] == 0:
		p = (q * (m - 1) + 2 * p) % MOD
		q = (2 * m * q) % MOD
	elif s1[i] == 0:
		p = (q * (m - s2[i]) + p) % MOD
		q = (m * q) % MOD
	elif s2[i] == 0:
		p = (q * (s1[i] - 1) + p) % MOD
		q = (m * q) % MOD
	elif s1[i] < s2[i]:
			p, q = 0, 1
	elif s1[i] > s2[i]:
			p, q = 1, 1

def mpow(a, n):
	if n == 0:
		return 1
	t = mpow(a, n // 2)
	t = (t * t) % MOD
	if n % 2 == 1:
		t = (t * a) % MOD
	return t

inv_q = mpow(q, MOD - 2)
r = (p * inv_q) % MOD

print(r)

