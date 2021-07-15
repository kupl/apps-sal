s = list(input())
l = len(s)

if l%2:
	f = 0
else:
	f = -1

s1 = ''
while s:
	s1 += s.pop(f)
	if f==0:
		f=-1
	else:
		f=0
	
print(s1[::-1])

