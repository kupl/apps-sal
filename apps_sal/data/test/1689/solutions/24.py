n = int(input())
b = True
ans = False
A = []
for i in range(n):
	s = input()
	if s[0] == 'O' and s[1] == 'O' and b:
		A.append("++|{0}{1}".format(s[3], s[4]))
		b = False
		ans = True
	elif 	s[3] == 'O' and s[4] == 'O' and b:
		A.append("{0}{1}|++".format(s[0], s[1]))
		b = False
		ans = True
	else:
		A.append(s)	
if ans:
	print("YES")
	for i in A:
		print(i)
else:
	print("NO")	

