N, X = map(int, input().split())
x = list(map(int, input().split()))
import math
for i in range(N):
	x[i] -= X
ans = x[0]
for i in range(1, N):
	ans = math.gcd(ans, x[i])
print(abs(ans))
