x = int(input())
expotential = [0] * (x + 1)
expotential[1] = 1
for b in range(2, x+1):
	t = b * b
	while(t <= x):
		expotential[t] = 1
		t *= b
for i in range(x, 0, -1):
	if expotential[i]:
		print(i)
		break
