a, b, c = map(int, input().split(' '))
p = 998244353

def calc (a, b) :
	if a > b:
		a, b = b, a
	ans = 0
	tmp = 1
	for i in range(a + 1):
		ans = (ans + tmp) % p
		tmp = tmp * (a - i) * (b - i) * pow(i + 1, p - 2, p) % p
	return ans

ans = calc(a, b) * calc(b, c) * calc(a, c) % p

print(ans)
