def multi(nu):
	r = 1
	for x in str(nu):
		r *= int(x)
	return r

n = int(input())
res = multi(n)
for i in range(100):
	aa = n-(n%(10**i))-1
	if aa >= 0:
		res = max(res, multi(aa))
print(res)

