n = int(input())

l = 0
r = n

def eats(n, k):
	res = 0
	while n > 0:
		if n < k:
			res += n
			n = 0
		else:
			res += k
			n -= k
			n -= n//10
	return res

while r-l > 1:
	mid = (r + l) // 2
	if eats(n, mid) >= (n+1) // 2:
		r = mid
	else:
		l = mid

print(r)

