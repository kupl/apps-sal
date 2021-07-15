def GCD(a, b):
	while a != 0 and b != 0:
		if a > b:
			a %= b
		else:
			b %= a
	return a + b

s = input().split(' ')
n = int(s[0])
m = int(s[1])
k = int(s[2])

divided = False

if 2 * n * m % k != 0:
	print("NO")
	return

if k % 2 == 0:
	k = k // 2
	divided = True

k1 = GCD(n,k);
k2 = k // k1;
x = n // k1;
y = m // k2;
if not divided:
	if 2 * x <= n:
		x *= 2
	elif 2 * y <= m:
		y *= 2
	else:
		print("NO")
		return

print("YES")
print(0, y)
print(0, 0)
print(x, 0)
