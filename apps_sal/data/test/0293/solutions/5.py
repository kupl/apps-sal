n = int(input())
i,t,s = [0] * 3
r = []
while 1 > 0:
	i += 1
	n -= i * i
	if n < 0 : break
	t += i
	m = n  //  t 
	if  m * t !=  n :  continue
	r.append((i, m + i))
	if m > 0:
		r.append((m+i, i))	

print(len(r))
r.sort()
for m, n in r:
	print("%d %d" % (m , n))

