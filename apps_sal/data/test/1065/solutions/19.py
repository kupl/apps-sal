
def binn(p):
	nonlocal n, k, m, d
	l = 0
	r = m
	while l + 1 < r:  
		m1 = (l + r) // 2 
		if (m1 * p * k + m1 - 1 >= n):
			r = m1
		else:
			l = m1
	return r


def binn1(x, p):
	nonlocal n, k, m, d
	l = x 
	r = m + 1
	while l + 1 < r:
		m1 = (l + r) // 2
		if (m1 * p + (k - 1) * (p - 1) * m1 <= n):
			l = m1
		else:
			r = m1
	return l 


n, k, m, d = map(int, input().split()) 
ans = -1e18
for i in range(1, d + 1): 
	x = binn(i)
	x1 = binn1(x, i)
	if (x1 * i + (k - 1) * (i - 1) * x1 <= n and x1 * i * k + x1 - 1 >= n):
		ans = max(ans, x1 * i)	                  

print(ans)
