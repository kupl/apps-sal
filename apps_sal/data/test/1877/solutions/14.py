n = int(input())
s = list(input())

cur = [0,0]
f  = 0
c = 0
for i in s:
	if i=='U':
		cur[1]+=1
	else:
		cur[0]+=1
	if cur[0]>cur[1]:
		if f==2:
			c+=1
		f = 1
	elif cur[1]>cur[0]:
		if f==1:
			c+=1
		f = 2
print (c)
