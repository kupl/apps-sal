k, p = list(map(int, input().split()))

def cd(n):
	res = 0
	while n > 0:
		res += 1
		n //= 10
	return res

def rev(n):
	res = 0
	while n > 0:
		res*= 10
		res += n % 10
		res %= p
		n //= 10
	return res

ans = 0
for i in range(1, k + 1):
	ans += i * 10**cd(i) + rev(i)
	ans %= p
print(ans)
