x=input()
for i in range(len(x)):
	#print(i)
	count=len(x)-i-1
	if x[len(x)-i-1]!='0':
		break
#print(count)
x=x[:count+1]
if x==x[::-1]:
	print('YES')
else:
	print('NO')
