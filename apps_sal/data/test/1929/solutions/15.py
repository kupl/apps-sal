n, t, c = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

k = 0
p = 0
i = 0

for i in a:
	if i <= t:
		p += 1
	else:
		if p >= c:
			k += p - c + 1
		p = 0

if p >= c:
	k += p - c + 1

print (k)
