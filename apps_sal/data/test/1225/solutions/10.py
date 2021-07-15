def myfunc(N):
	if(N  <= 1):
		return 1
	return 2 * myfunc(int(N/2)) + 1

def __starting_point():
	N = int(input())
	print(myfunc(N))
__starting_point()
