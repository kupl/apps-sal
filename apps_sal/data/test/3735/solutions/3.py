def s(x):
	res = 0
	while x > 0:
		res += x % 10
		x //= 10
	return res

n = input()
ans = 9*(len(n)-1)
n = int(n) - 10**(len(n) - 1) + 1
print(ans + s(n))
