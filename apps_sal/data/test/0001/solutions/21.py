n = int(input())

def sumd(n):
	j = n
	sumn = 0
	while j:
		sumn += j % 10
		j //= 10
	return sumn

j = n
strn = str(n)
l = len(strn)
sumn = sumd(n)

stra = [i for i in str(n)]
i = 1
while i < l and stra[i] == '9':
	i += 1
if (i != l):
	stra[i - 1] = str(int(stra[i - 1]) - 1)
	while i < l:
		stra[i] = '9'
		i += 1

ss = ''
for i in range(l):
	ss += stra[i]
if ss[0] == '0':
	ss = ss[1:]
sn = int(ss)

if sn < n and sumd(sn) <= sumn:
	ss = strn
	sn = n

print(ss)

