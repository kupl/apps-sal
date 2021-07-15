def gcd(a, b):
	while b:
		a, b = b, a % b
	return a


def razl(n):
	cnt = 0
	i = 1
	while (i * i < n):
		if (n % i == 0):
			cnt += 2
		i += 1
	if (i * i == n):
		cnt += 1
	return cnt


n = int(input())
ans = 0
for i in map(int, input().split()):
	ans = gcd(ans, i)
print(razl(ans))
