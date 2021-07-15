def fact(x):
	l = []
	i = 2
	while i * i <= x:
		while x % i == 0:
			x //= i
			l.append(i)
		i += 1
	if x != 1:
		l.append(x)
	return l
n = int(input())
print(*fact(n), sep='')
