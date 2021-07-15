# your code goes here
a = (input())
b = (input())
j = 0
for i in range(len(a)):
	if a[i] == '0':
		j+=1
	else: 
		break
a = a[j:]
j = 0
for i in range(len(b)):
	if b[i] == '0':
		j+=1
	else: 
		break
b = b[j:]
flag = 0
if len(a)> len(b):
	print (">")
elif len(a)<len(b):
	print ("<")
else:
	for i in range(len(a)):
		if (a[i]>b[i]):
			flag = 1
			break
		elif (a[i]<b[i]):
			flag = 2
			break
		else:
			continue
	if (flag == 0):
		print ("=")
	elif (flag == 1):
		print (">")
	else:
		print ("<")

