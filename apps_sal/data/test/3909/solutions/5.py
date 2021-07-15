n = int(input())
k = 1
while not n % k:
	k *= 3
print(n // k + 1)

