a,b = map(int,input().split())
s = input()
c = 0

def is_int(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

for i in range(a):
	if is_int(s[i]) == True:
		c += 1
for i in range(a+1,a+b):
	if is_int(s[i]) == True:
		c += 1
if s[a] == '-' and c == len(s) - 2:
	print('Yes')
else:
	print('No')
