n, m = map(int, input().split(' '))
mod = int(1e9 + 7)

l = [1] * (m+1)
for i in range(1, m+1):
	l[i] = (l[i-1] * i) % mod

l2 = [1] * (m+1)
l2[m] = pow(l[m], mod-2, mod)
for i in range(m-1, 0, -1):
	l2[i] = (l2[i+1] * (i+1)) % mod

s = 0
for k in range(n+1):
	n_choose_k = (l[n] * l2[k] * l2[n-k]) % mod
	m_perm_k = (l[m] * l2[m-k]) % mod
	mk_perm_nk = (l[m-k] * l2[m-n]) % mod
	s += ((-1) ** k * n_choose_k * m_perm_k * mk_perm_nk ** 2 ) % mod 

print(s % mod)
