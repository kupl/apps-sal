s = input()
a = s.count('1')
l = []
for i in s:
	if i != '1':
		l.append(i)
b = ['1']*a
c = len(l)
for i in range(len(l)):
	if l[i] == '2':
		c = i
		break
ans = l[0:c] + b + l[c:len(l)]
for i in ans:
	print(str(i), end = '')

