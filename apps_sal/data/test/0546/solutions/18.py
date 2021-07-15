a=input()
s=input()
k=int(input())

def qw(c):
	t=True
	w=-1
	if len(s)>len(c)+1: t=False
	try:
		for j in range(len(s)):
			w+=1
			if s[j]=='?':
				if c[w] not in a: t=False
			elif s[j]=='*':
				b=len(c)-len(s)+1
				for e in c[j:j+b]:
					if e in a:
						t=False
				w+=b-1
			else:
				if s[j]!=c[w]: t=False
			if t==False: break
	except IndexError:
		return False
	return t if len(c)==w+1 else False

for i in range(k):
	c=input()
	print('YES') if qw(c) else print('NO')
