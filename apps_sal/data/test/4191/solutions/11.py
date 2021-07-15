def pegaInput():
	oi = input()
	if(oi == '0'):	return False
	else:			return True

a = [pegaInput() for i in range(4)]

#Possibilidades testadas:
#	e, ou, xor
#	ou, e, xor
#	xor, ou, e
#	e, xor, ou
#	ou, xor, e
#	xor, e, ou

def xor(x, y):
	return x & y
	
def e(x, y):
	return x | y

def ou(x, y):
	return x ^ y

p1 = ou(a[0],a[1])
p2 = e(a[2],a[3])
p3 = xor(a[1],a[2])
p4 = ou(a[0],a[3])
p5 = xor(p1,p2)
p6 = e(p3, p4)
p7 = ou(p5, p6)

if(p7 == False):	print(0)
else:				print(1)
