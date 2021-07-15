
n = int(input())
s = input()
flag = False
for i in range(n):
	for k in range(1,n):
		if i + 4*k < n:
			if s[i] == '*' and s[i + k] == '*' and s[i + 2*k] == '*' and s[i + 3*k] == '*' and s[i + 4*k] == '*':
				flag = True  
if flag == True:
	print('yes')
else:
	print('no')
