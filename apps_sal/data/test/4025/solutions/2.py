A = list(map(int, input().split()))
X = [0, 1, 2, 0, 2, 1, 0]
a, b, c = A
res = min(min(a//3, b//2), c//2)
a -= res*3
b -= res*2
c -= res*2
res *= 7
A = [a, b, c]
maxc = -1
for i in range(0, 7):
	A0 = A[:]
	c = 0
	while True:
		if A0[X[i]] > 0:
			A0[X[i]] -= 1
			c += 1
			i = (i + 1) % 7
		else:
			break
	if c > maxc:
		maxc = c
print(res + maxc)
