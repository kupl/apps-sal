def f(a):
	flag = False
	for i in str(a):
		if (i == "8"):
			flag = True
	return flag


a = int(input())
# a = 18
d = 1
while not f(a + d): #and not f(a - d):
	d += 1
print(d)

