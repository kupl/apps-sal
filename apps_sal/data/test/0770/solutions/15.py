def main():
	n=input()
	n=int(n)
	a=list(map(int,input().split(" ")))
	a=list(a)
	if 0 in a:
		if len(a) == a.count(0):
			print(0)
			return
		pass
	pass
	a=list(map(str,a))
	a="".join(a)
	a=a.split("0")
	s=0
	for x in a:
		s+=len(x)
	pass
	z=len(a)-a.count('')
	print(s+z-1)
	pass
	
main()



