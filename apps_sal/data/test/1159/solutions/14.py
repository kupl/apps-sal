n = int(input())
odp = []
for i in range(n - 1):
	odp.append([i + 1, i + 2])
odp.append([n, 1])
k = n
def prime(x):
	i = 2
	while i ** 2 <= x:
		if x % i == 0:
			return False
		i += 1
	return True
primes = [0] * 50000
for i in range(50000):
	primes[i] = (1 if prime(i) else 0)
w = (n + 2) // 2
m = 1
while w <= n:
	if primes[k] == 1:
		break
	else:
		odp.append([m, w])
		m += 1
		w += 1
		k += 1
print(len(odp))
for i in range(len(odp)):
	print(odp[i][0], odp[i][1])
