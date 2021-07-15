n = int(input())
c = {}
c['polycarp'] = []
for i in range(n):
	s = input().split(' reposted ')
	s[0] = s[0].lower()
	s[1] = s[1].lower()
	if s[0] not in c:
		c[s[0]] = []
	c[s[1]] += [c[s[0]]]
answ = str(c['polycarp'])
count = 0
m = 0
for i in answ:
	if i == '[':
		count += 1
		if count > m:
			m = count
	elif i == ']':
		count -= 1
print(m)
