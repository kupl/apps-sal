x=str(input())
x=x.replace("RRR","k")
if "k" in x:
	print(3)
else:
	x=x.replace("RR","k")
	if "k" in x:
		print(2)
	else:
		x=x.replace("R","k")
		if "k" in x:
			print(1)
		else:
			print(0)
