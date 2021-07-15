def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a

[n, m] = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]
g = 0
for i in range(n - 1):
	g = gcd(g, x[i + 1] - x[i])
cnt = 1
for i in input().split():
	j = int(i)
	if g % j == 0:
		print ("YES")
		print (x[0], cnt, sep = ' ')
		return
	cnt += 1
print ("NO")
