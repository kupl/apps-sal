R = lambda:map(int, input().split())
n = int(input())
A = list(R())
if n == 1 or n == 2:
	print(0)
	quit()
minn = int(1e9 + 1)
for i in range(-1,2):
	for j in range(-1, 2):
		if (A[0] + i - A[-1] - j) % (n - 1):
			continue
		f = A[0] + i
		g = A[-1] + j
		cnt = abs(i) + abs(j)
		d = (g - f) // (n - 1)
		for x in range(1, n - 1):
			f += d
			if abs(f - A[x]) > 1:
				break
			elif abs(f - A[x]) == 1:
				cnt += 1
		else:
			minn = min(minn, cnt)
if minn == int(1e9 + 1):
	print(-1)
else:
	print(minn)
