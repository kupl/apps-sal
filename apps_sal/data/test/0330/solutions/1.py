p, y = list(map(int, input().split()))
def f(x):
	i = 2
	while i <= p and i * i <= y:
		if x % i == 0:
			return False
		i += 1
	return True
ind = False		
for i in range(y, p, -1):
	if f(i):
		print(i)
		ind = True
		break
if not ind:
	print(-1)

