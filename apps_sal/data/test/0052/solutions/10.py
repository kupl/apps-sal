n = int(input())

def f(t, k):
	return t*(t-1)//2 + t*((1<<k)-1)

ans = set()
for k in range(60):
	l = 0
	r = n
	p = 0
	while l <= r:
		t = (l+r)//2
		if f(t, k) <= n:
			p = t
			l = t+1
		else:
			r = t-1
	if p % 2 == 1 and f(p, k) == n:
		ans.add(p * (1<<k))

for x in sorted(ans):
	print(x)

if not ans:
	print(-1)
