n,p = list(map(int, input().split()))
a = list(map(int, input().split()))

x = a[0] % p
y = sum(a[1:]) % p
s = x+y
for i in range(1, n-1):
	x = (x+a[i]) % p
	y = (y-a[i]) % p
	s = max(s, x+y)
print(s)

