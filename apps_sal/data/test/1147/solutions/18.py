n, x, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

a.sort()

ans = 0
s, t = 0, 0
for j in range(n):
	cur = ((a[j] // x) - k) * x
	
	while s < n and a[s] <= min(cur,a[j]):
		s += 1
		
	while t < n and a[t] <= min(cur + x, a[j]):
		t += 1
	
	ans += (t-s)
	
print(ans)
