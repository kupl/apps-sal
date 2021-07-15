n = int(input())
k = int(input())
A = int(input())
B = int(input())

ans = 0
if k == 1:
	print(A*(n-1))
	return

while n > 1:
	subt = (n % k)
	ans += A * subt
	n -= (n%k)
	ans += min(A * (n - (n // k)),B)
	n //= k

if n == 0:
	ans -= A

print(ans)
