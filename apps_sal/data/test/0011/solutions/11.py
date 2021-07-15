def gcd(a, b):
	if a == 0:
		return b
	if b == 0:
		return a
	return gcd(b, a % b)

def get_nok(a, b):
	return (a * b) // gcd(a, b)

n, a, b, p, q = list(map(int, input().split()))

if p < q:
	a, b = b, a
	p, q = q, p


nok = get_nok(a, b)

t = n // a
minus = n // nok
c = n // b
print(t * p + q * (c - minus))



