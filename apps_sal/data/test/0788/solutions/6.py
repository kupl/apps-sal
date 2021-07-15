s = input()
p = 0
t = 0
for i in s[1:]:
	if i == '0':
		p *= 10
	t += p
	p = int(i)
print(t+p+1)
