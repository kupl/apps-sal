def mi():
	return map(int, input().split())

n,m = mi()
a = list(mi())
s = 0
t = []
for i in a:
	s+=i
	t.append(s//m)
for i in range(n):
	if i==0:
		print (t[i], end = ' ')
	else:
		print (t[i]-t[i-1], end=  ' ')
