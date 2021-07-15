l, r, x, y = list(map(int, input().split()))
def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a
divisor = [1, y]
i = 2
count = 0
while i * i <= y:
	if y % i == 0:
		divisor.append(i)
		if i * i != y:
			divisor.append(y // i)
	i += 1		
for j in divisor:
	if j >= l and j <= r and j % x == 0:
		a = (x * y) // j
		if a >= l and a <= r and gcd(a, j) == x:
			count += 1
print(count)		


			



