def li ():
	return list (map (int, input ().split ()))


def num ():
	return map (int, input ().split ())


def nu ():
	return int (input ())

mm = 1000000007


def solve ():
	t = 1
	for it in range (t):
		n=nu()
		cc=0
		for i in range(2,n):
			cc+=i*(i+1)
		print(cc)



def __starting_point():
	solve ()
__starting_point()
