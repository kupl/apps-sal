from math import factorial as f

def main():
	a=input()
	b=input()
	ap=a.count('+')
	an=a.count('-')
	bp=b.count('+')
	bn=b.count('-')
	tandatanya=b.count('?')
	if tandatanya == 0:
		if ap-an != bp-bn:
			print ("%.9f" % (0))
		else:
			print ("%.9f" % (1))
		return
	probab=float(1/pow(2,tandatanya))
	x=(ap-an-(bp-bn)+tandatanya)//2
	y=tandatanya-x
	if x < 0 or y < 0:
		print ("%.9f" % (0))
		return
	probab*=f(tandatanya)/(f(x)*f(y))  
	print ("%.9f" % (probab))

main()
