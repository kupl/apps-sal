from math import sqrt

n = int(input())
ans = [1, n * (n+1) // 2]
divisor = []

for i in range(2, int(sqrt(n))+1):
	if n % i == 0:
		divisor.append(i)
		if i != n//i:
			divisor.append(n//i)

for d in divisor:
	ans.append(((n//d-1) * (n//d) // 2) * d + (n//d))

ans.sort()
print(*ans)
