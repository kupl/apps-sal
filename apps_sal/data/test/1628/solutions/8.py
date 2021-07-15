S = input()

ctr = 0

for i in S:
	if(i=="x"):
		ctr+=1
	else:
		ctr-=1

if(ctr<0):
	print("y"*(-ctr))
else:
	print("x"*ctr)
