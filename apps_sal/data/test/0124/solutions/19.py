import math,time

def main():
	x,y,z = list(map(int, input().split()))
	a,b,c = list(map(int, input().split()))
	if x>a:
		print("NO")
		return
	else:
		a -= x
		u = a+b
		if y>u:
			print("NO")
			return
		else:
			u -= y
			u += c
			if z>u:
				print("NO")
				return
			else:
				print("YES")

def __starting_point():
	start_time = time.time()
	main()
	#print("--- %s seconds ---" % (time.time() - start_time))


__starting_point()
