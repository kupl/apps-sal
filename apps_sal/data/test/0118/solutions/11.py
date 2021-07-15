line = input().split()
t = int(line[0])
s = int(line[1])
x = int(line[2])
x = x-t
if x >=0 and (x%s==0 or ( x!=1 and (x-1)%s==0)):
	print ('YES')
else:
	print ('NO')
