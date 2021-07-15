n, k = map(int,input().split())
s = [i for i in input()]

def jk(a,b):
	if a == 'R':
		if b == 'P':
			return b
		else:
			return a
	elif a == 'P':
		if b == 'S':
			return b
		else:
			return a
	else:
		if b == 'R':
			return b
		else:
			return a

while k:
	t = s + s;
	for i in range(n):
		s[i] = jk(t[i * 2],t[i * 2 + 1])
	k -= 1
print(s[0])
