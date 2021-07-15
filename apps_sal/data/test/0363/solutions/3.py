def f(n):
	if n < 10:
		return n
	k = 10 ** (len(str(n)) - 1)
	return len(str(n)) * ((n % k) + 1) + f(n - (n % k) - 1)

n = int(input())
print(f(n))
