n, m = (int(x) for x in input().split())
a = [int(x) for x in input().split()]

#print(n, m, a)

d = {}

for ai in a:
	d.setdefault(ai, 0)
	d[ai] += 1
	
	ans = 0
	if len(d) >= n:
		ans = 1
		d = {k: v-1 for k, v in d.items() if v > 1}
	
	print(ans, end="")

#print(d)
