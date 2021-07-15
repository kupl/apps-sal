def f(x1,k1):
	x = x1
	k = k1
	if k==0:
		return int(''.join(x))
	y = len(x)
	i = 0
	while i < y and x[i] == '9':
		i += 1
	if i == y:
		return int(''.join(x))
	while i < y and k>0:
		j = i+1
		m = i
		while j < y and j <= i+k:
			if x[j] > x[m]:
				m = j
			j += 1
		if m != i:
			k -= m-i
			while m > i:
				h = x[m]
				x[m] = x[m-1]
				x[m-1] = h
				m -= 1
			
		i+=1
	return int(''.join(x))

x = input()
i=len(x)-1
while x[i] != ' ':
	i -= 1

k = int(x[i+1:])
x = list(x[:i])

print(f(x,k))
