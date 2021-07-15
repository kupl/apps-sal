x, k = list(map(int, input().split()))
a = [0] * x
q = x - 1
for i in range(k):
	s = list(map(int, input().split()))
	a[s[1] - 1] = 1
	if len(s) == 3:
		a[s[2] - 1] = 1
	q-= len(s) - 1
p = 0
for i in range(x - 1):
	if a[i] == 0:
		p += 1
		if a[i + 1] == 0:
			a[i + 1] = 1
print(p, q)

