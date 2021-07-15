n = int(input())
A = list(map(int, input().split()))
a, b, c = 0, 0, 0
i = 1
while i <= n:
	a += A[i - 1]
	i += 3
i = 2
while i <= n:
	b += A[i - 1]
	i += 3
i = 3
while i <= n:
	c += A[i - 1]
	i += 3
if a >= b and a >= c:
	print("chest")
elif b >= a and b >= c:
	print("biceps")
else:
	print("back")
