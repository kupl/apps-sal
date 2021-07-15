l = input().replace(';',',').split(',')
res1 = []
res2 = []

def isValid(a):
	if a.startswith("0") and a != "0":
		return False
	else:
		return a.isnumeric()



for i in range(0,len(l)):
	if isValid(l[i]):
		res1.append(l[i])
	else:
		res2.append(l[i])


if len(res1) == 0:
	print("-")
else:
	print("\""+",".join(res1)+"\"")

if len(res2) == 0:
	print("-")
else:
	print("\""+",".join(res2)+"\"")


