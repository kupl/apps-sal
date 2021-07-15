user = int(input())
n = list(input().split(" "))
l = len(n)-1
if int(n[0]) == 3 and int(n[l])!=3:
	n.reverse()
r = 0
a = 0
c = 0
res = []
for i in n:
	if int(i) == 0:
		r = r + 1
		a = 0
		c = c + 1
	if int(i) == 1 :
		if a == 0 or a!=2:
			a = 2
			c = c + 1
		else:
			r = r + 1 
			a = 0
			c = c + 1
	if int(i) == 2:
		if a == 0 or a!=1:
			a = 1
			c = c + 1
		else:
			r = r + 1
			a = 0
			c = c + 1
	if int(i) == 3:
		if a==0:
			while c < len(n) and n[c] == 3:
				c = c + 1
			if c < len(n):
				if n[c] == 1:
					a = 2
				elif n[c] == 2:
					a = 1
		elif a!=1:
			a = 1
		elif a!=2:
			a = 2
print(r)
