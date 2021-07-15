import math, sys
def main():
	n = int(input())
	x = int(input())
	d0 = [0,1,2,2,1,0]
	d1 = [1,0,0,1,2,2]	
	d2 = [2,2,1,0,0,1]
	if (d0[n%6]==x):
		print(0)
	elif (d1[n%6]==x):
		print(1)
	else:
		print(2)
	
			
def __starting_point():
	main()

__starting_point()
