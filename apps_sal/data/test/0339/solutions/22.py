n = int(input())
k = int(input())
c1 = int(input())
c2 = int(input())
if k == 1:
	k += n
ans = 0
while n > 1:
	if n > k:
		temp = n % k
		ans += temp * c1
		n -= temp
	if n % k == 0:
		ans += min(c2, (n - n // k) * c1)
		n //= k
	else:
		ans += (n - 1) * c1
		n = 1
print(ans)
