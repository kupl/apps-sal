n,t = list(map(int, input().split()))
a = list(map(int, input().split()))

_ = min(a)
r = 0
s = sum(a)
n_ = n
while t >= _:
	v = int(t/s)
	r += v*n_
	t -= v*s
	for i in range(n):
		if a[i] == 0:
			continue
		if t >= a[i]:
			r += 1
			t -= a[i]
		else:
			n_ -= 1
			s -= a[i]
			a[i] = 0
print(r)
